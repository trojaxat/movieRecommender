from src.models.preferencesModel import Preferences


class User:
    """Class for user"""

    def __init__(self, id, name, numberOfRatings, preferences=Preferences):
        self.id = id
        self.name = name
        self.numberOfRatings = numberOfRatings
        self.preferences = preferences
