from app.models.base_model import BaseModel
from app.models.user import User

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner_id):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.reviews = []
        self.amenities = []

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value or not isinstance(value, str) or len(value) > 100:
            raise ValueError("Title is required and must be a string with max 100 characters")
        self.__title = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if value is not None and (not isinstance(value, str) or len(value) > 500):
            raise ValueError("Description must be a string with max 500 characters")
        self.__description = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Price must be a positive number")
        self.__price = value

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, (int, float)) or not (-90.0 <= value <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0")
        self.__latitude = value

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (int, float)) or not (-180.0 <= value <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0")
        self.__longitude = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("Owner must be a User instance")
        self.__owner = value

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

