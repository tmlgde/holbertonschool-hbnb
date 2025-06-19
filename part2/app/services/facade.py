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
    # Placeholder for logic to create a place, including validation for price, latitude, and longitude
    pass

    def get_place(self, place_id):
    # Placeholder for logic to retrieve a place by ID, including associated owner and amenities
    pass

    def get_all_places(self):
    # Placeholder for logic to retrieve all places
    pass

    def update_place(self, place_id, place_data):
    # Placeholder for logic to update a place
    pass
