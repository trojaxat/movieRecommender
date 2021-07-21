from src.models.dataframeModel import DataFrame
from src.models.moviemodel import Movie
import numpy as np
from sklearn.decomposition import NMF
from IPython.display import display as d


class Movies(DataFrame):
    """Class for movies"""

    def __init__(self, df):
        super().__init__(df)

    def getMovies(self, amount):
        movies = []
        for movieFromDf in self.df.iterrows():
            movie = Movie(
                movieFromDf[0],
                movieFromDf[1].title,
                movieFromDf[1].genres)
            movies.append(movie)
            if len(movies) == amount:
                break
        return movies

    def getRecommendationsArray(self, R):
        # NMF model
        model = NMF(n_components=2, init='random')
        model.fit(R)
        Q = model.components_  # movie-genre matrix

        # Creates a new user and gives recommendations based on avg
        new_user = np.full(shape=(1, R.shape[1]), fill_value=R.mean().mean())
        user_P = model.transform(new_user)

        actual_recommendations = np.dot(user_P, Q)
        return np.argsort(actual_recommendations)[0]

    def getMoviesArray(self, df, amount):
        return np.array(df['movieId'].head(amount))

    def getRecommendationsReadable(self, recommendationArray, amount):
        movies = self.df

        if len(recommendationArray) < amount:
            amount = len(recommendationArray)

        recommendationsList = []
        for index in range(amount):
            try:
                movie_id = recommendationArray[index]
                movie = Movie(
                    movie_id, movies.loc[movie_id].title, movies.loc[movie_id].genres)
                recommendationsList.append(movie)
            except Exception:
                print("Movie not found", recommendationArray[index])

        return recommendationsList
