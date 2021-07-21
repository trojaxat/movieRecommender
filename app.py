from src.models.moviemodel import MOVIE_GENRES
from flask import Flask, render_template, session
from flask_bootstrap import Bootstrap
from flask_session import Session
from helper_functions import getSessionRecommendations, checkRecommendationArgs, getVerySpecialImage, checkPreferenceArgs
import secrets
from consts import MOVIES_TO_CHOOSE_FROM

SESSION_TYPE = 'filesystem'
# session.clear()


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(__name__)
    app.secret_key = secrets.token_urlsafe(32)
    Session(app)
    Bootstrap(app)
    return app


app = create_app()


@ app.route('/')
def index():
    recommendations = getSessionRecommendations()
    userName = recommendations.user.name
    verySpecialImage = getVerySpecialImage()

    return render_template(
        'home.html',  xkcd=verySpecialImage, name=userName)


@ app.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    recommendations = getSessionRecommendations()
    genre, rating = checkRecommendationArgs()
    recommendations.genre = genre
    recommendations.ratingValue = rating

    recList = recommendations.getSpecificRecommendations()

    return render_template(
        'recommendations.html',
        recommendations=recList,
        name=recommendations.user.name,
        info=recommendations.restrictions,
        genres=MOVIE_GENRES)


@ app.route("/users")
def users():
    recommendations = getSessionRecommendations()
    usersList = recommendations.users.getUsersWithMostRatings(10)

    return render_template('users.html', name=recommendations.user.name, users=usersList)


@ app.route("/movies")
def movies():
    recommendations = getSessionRecommendations()
    movies = recommendations.movies.getMovies(15)

    return render_template('movies.html', name=recommendations.user.name, movies=movies)


@ app.route("/preferences", methods=['GET', 'POST'])
def preferences():
    recommendations = getSessionRecommendations()
    preferences = checkPreferenceArgs()
    if preferences is not None:
        recommendations.user.preferences = preferences

    suggestions = recommendations.getPersonalizedRecommendations()

    return render_template(
        'preferences.html',
        name=recommendations.user.name,
        suggestions=suggestions,
        preferences=preferences,
        movie_names=MOVIES_TO_CHOOSE_FROM)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
