
MOVIE_GENRES = [None, "Action",
                "Comedy", "Crime", "Drama", "Thriller"]


class Movie:
    """Class for a movie"""

    def __init__(self, id, title, genres):
        self.id = id
        self.title = title
        self.genres = genres
