#!/usr/bin/python3
from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity

class HBnBFacade:

    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Create a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    # Retrieve a user by ID
    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    # Retrieve a user by email
    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    # Get all users
    def get_all_users(self):
        return self.user_repo.get_all()

    # Update a user
    def update_user(self, user_id, data):
        user = self.user_repo.get(user_id)
        if user is None:
            return None
        for key, value in data.items():
            if hasattr(user, key):
                setattr(user, key, value)
        return user

    # Create an amenity
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    # Retrieve an amenity by ID
    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    # Retrieve all amenities
    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    # Update an amenity
    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if amenity is None:
            return None
        for key, value in amenity_data.items():
            if hasattr(amenity, key):
                setattr(amenity, key, value)
        return amenity

    def create_place(self, place_data):
        owner_id = place_data.get("owner_id")
        owner = self.user_repo.get(owner_id)
        if not owner:
            raise ValueError("Invalid owner_id: User not found")
        price = place_data.get("price")
        latitude = place_data.get("latitude")
        longitude = place_data.get("longitude")
        if latitude is None or not isinstance(latitude(int, float)) or not (-90 <= latitude >= 90):
            raise ValueError("Latitude must be between -90 and 90")
        if price is None or not isinstance(price(int, float)) or price < 0:
            raise ValueError("Invalid price")
        if longitude is None or not isinstance(longitude(int, float)) or note (-180 <= longitude >= 180):
            raise ValueError("Longitude must be between -180 and 180")
            amenity_ids = place_data.get("amenities")
    if not isinstance(amenity_ids, list):
        raise ValueError("Amenities must be a list of IDs")

    amenities = []
    for amenity_id in amenity_ids:
        amenity = self.amenity_repo.get(amenity_id)
        if amenity is None:
            raise ValueError(f"Amenity with ID {amenity_id} not found")
        amenities.append(amenity)

    place = Place(
        title=title,
        description=description,
        price=price,
        latitude=latitude,
        longitude=longitude,
        owner_id=owner_id,
        amenities=amenities_objs
    )   
    self.place_repo.add(place)
    return place


    def get_place(self, place_id):
        def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            return None

        owner = place.owner

        amenities = []
        for amenity in place.amenities:
            amenities.append({"id": amenity.id, "name": amenity.name})

        return {
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "price": place.price,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner": {
                "id": owner.id,
                "first_name": owner.first_name,
                "last_name": owner.last_name,
                "email": owner.email,
            },
            "amenities": amenities,
        }

    def get_all_places(self):
        places = self.place_repo.get_all()
        return = [
                {
                    "id": place.id,
                    "title": place.title,
                    "latitude": place.latitude,
                    "longitude": place.longitude,
                }
                for place in places
            ]

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        if "price" in place_data:
            price = place_data["price"]
            if not isinstance(price(int, float) or price < 0:
                    return None

        if "latitude" in place_data:
            latitude = place_data["latitude"]
            if not isinstance(latitude(int, float) or not (-90 <= latitude <= 90):
                return None

        if "longitude" in place_data:
            longitude = place_data["longitude"]
            if not isinstance(longitude(int, float) or not (-180 <= longitude <= 180):
                return None

        self.place_repo.update(place_id, place_data)
        return self.place_repo.get(place_id)
