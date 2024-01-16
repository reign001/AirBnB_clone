#!/usr/bin/python3
"""this defines the place class"""

class Place(BaseModel):
    """Represents a place.
        Attributes:
                city_id (string): the City.id
                user_id (string): the User.id
                name (string): the name of the place
                description (string): the description of the place
                number_rooms (integer): the number of room of the place
                number_bathrooms (integer):the number of bathrooms of the place
                max_guest (int): The maximum number of guests of the place.
                price_by_night (int): The price by night of the place.
                latitude (float): The latitude of the place.
                longitude (float): The longitude of the place.
                amenity_ids (list): A list of Amenity ids.
    """

        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
