from src.models.dataframeModel import DataFrame
import pandas as pd
from IPython.display import display as d


class Ratings(DataFrame):
    """Class for ratings"""

    def __init__(self, df):
        super().__init__(df)

    def setAverageRatings(self):
        df = self.df
        df['average_rating'] = ''
        df['average_rating'] = df.groupby(
            ['movieId'])['rating'].transform('mean')
        self.df = df

    def getAverageRatings(self):
        if 'average_rating' not in self.df:
            self.setAverageRatings()

        return self.df

    @staticmethod
    def limitOptionsRating(ratingsDf, ratingValue):
        lowerBound = int(float(ratingValue)) - 0.5
        upperBound = int(float(ratingValue)) + 0.5
        df = ratingsDf
        df = df[df['average_rating'].between(lowerBound, upperBound)]
        df = df.drop_duplicates('movieId')

        return df

    @staticmethod
    def limitOptionsGenre(df, movies, genre):
        movies_df = Ratings.getMoviesIdArrayFromGenre(movies, genre)
        df = pd.merge(df, movies_df, on="movieId", how='outer')
        df = df.drop_duplicates('movieId')

        return df.dropna()

    def limitOptions(self, movies, rating, genre):
        df = Ratings.limitOptionsGenre(self.df, movies, genre)
        df = Ratings.limitOptionsRating(df, rating)
        df = df.drop_duplicates('movieId')

        return df

    @staticmethod
    def getMoviesIdArrayFromGenre(movies_df, genre):
        if genre != None:
            df = movies_df[movies_df['genres'].str.contains(
                genre, regex=False)]
        return df
