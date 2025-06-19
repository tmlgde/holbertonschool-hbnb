#!/usr/bin/python3
from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place

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

    # Validation du prix
        price = place_data.get("price")
        if price is None or not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Invalid price: Must be a non-negative number")

    # Validation de la latitude
        latitude = place_data.get("latitude")
        if latitude is None or not isinstance(latitude, (int, float)) or not (-90 <= latitude <= 90):
            raise ValueError("Invalid latitude: Must be between -90 and 90")

    # Validation de la longitude
        longitude = place_data.get("longitude")
        if longitude is None or not isinstance(longitude, (int, float)) or not (-180 <= longitude <= 180):
            raise ValueError("Invalid longitude: Must be between -180 and 180")

    # PAS de pop() ici, car owner_id est requis dans le constructeur
        place = Place(**place_data)
        place.owner = owner  # Si tu as une propriété .owner à part

        self.place_repo.save(place)
        return place


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
        return [
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

        # Validation du prix
        if "price" in place_data:
            price = place_data["price"]
            if not isinstance(price, (int, float)) or price < 0:
                return None

    # Validation de la latitude
        if "latitude" in place_data:
            latitude = place_data["latitude"]
            if not isinstance(latitude, (int, float)) or not (-90 <= latitude <= 90):
                return None

    # Validation de la longitude
        if "longitude" in place_data:
            longitude = place_data["longitude"]
            if not isinstance(longitude, (int, float)) or not (-180 <= longitude <= 180):
                return None

    # Mise à jour des données
        self.place_repo.update(place_id, place_data)

    # Retourne le nouvel état du lieu
        return self.place_repo.get(place_id)

