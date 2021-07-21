from src.models.ratingsModel import Ratings
from IPython.display import display as d


class Recommendations:
    """Class for movie recommendations"""

    def __init__(self, movies, ratings, users, user):
        self.movies = movies
        self.ratings = ratings
        self.users = users
        self.user = user
        self.genre = None
        self.ratingValue = None
        self.recommendations = None
        self.restrictions = ""

    def getRecommendations(self, recommendationArray, amountWanted):
        recommendationsList = self.movies.getRecommendationsReadable(
            recommendationArray, amountWanted)
        self.recommendations = recommendationsList
        return recommendationsList

    def getPersonalizedRecommendations(self):
        suggestions = []
        return suggestions

    def getSpecificRecommendations(self, amount=10):
        if self.ratingValue is not None and self.genre is None:
            self.restrictions = f"Per rating value {self.ratingValue}"
            recommendationArray = self.getRatingRecommendationArray(amount)
        elif self.ratingValue is None and self.genre is not None:
            self.restrictions = f"Per genre {self.genre}"
            recommendationArray = self.getGenreArray(amount)
        elif self.ratingValue is not None and self.genre is not None:
            self.restrictions = f"Per genre {self.genre} and rating {self.ratingValue}"
            recommendationArray = self.getGenreRatingArray(amount)
        else:
            recommendationArray = self.getAverageRatingArray()

        recommendations = self.getRecommendations(
            recommendationArray, amount)

        return recommendations

    def getRatingRecommendationArray(self, amount):
        df = self.ratings.getAverageRatings()

        df = Ratings.limitOptionsRating(
            self.ratings.df, self.ratingValue)
        recommendationArray = self.movies.getMoviesArray(df, amount)

        return recommendationArray

    def getAverageRatingArray(self):
        df = self.ratings.df
        R = self.ratings.cleanData(df)
        self.restrictions = "Average Rating"

        return self.movies.getRecommendationsArray(R)

    def getGenreRatingArray(self, amount):
        df = self.ratings.limitOptions(
            self.movies.df, self.ratingValue, self.genre)

        return self.movies.getMoviesArray(df, amount)

    def getGenreArray(self, amount):
        df = Ratings.limitOptionsGenre(
            self.ratings.df, self.movies.df, self.genre)

        return self.movies.getMoviesArray(df, amount)
