from flask import request, session
from src.models.recommendationsModel import Recommendations
from src.models.ratingsModel import Ratings
from src.models.usersModel import Users
from src.models.userModel import User
from src.models.moviesModel import Movies
from consts import MOVIES, RATINGS
import requests
import json
from random import randint


def getSessionRecommendations():
    if not 'recommendations' in session:
        session['recommendations'] = Recommendations(
            Movies(MOVIES), Ratings(RATINGS), Users(RATINGS), User(1, "Dan Axford", 25))
    return session['recommendations']


def checkRecommendationArgs():
    genre = None
    rating = None
    if request.method == 'POST':
        if request.form.get('genre') != "None":
            genre = request.form.get('genre')

        if int(request.form.get('rating')) != 0:
            rating = request.form.get('rating')

    return genre, rating


def checkPreferenceArgs():
    preferences = None
    if request.method == 'POST':
        preferences = request.form.to_dict(flat=False)

    return preferences


def getVerySpecialImage():
    randomNumber = randint(1, 1000)
    url = f"https://xkcd.com/{randomNumber}/info.0.json"
    response = requests.get(url)
    jsonResponse = json.loads(response.content.decode('utf-8'))
    return jsonResponse['img']
