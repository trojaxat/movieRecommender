import os
import pandas as pd

MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
RATINGS = pd.read_csv(os.path.join(
    MAIN_DIR,
    'static/data/ratings_with_names.csv'))
MOVIES = pd.read_csv(os.path.join(
    MAIN_DIR, 'static/data/movies.csv'), index_col=0)
SECRET_KEY_EXAMPLE = b'_5#y2L"F4Q8z\n\xec]/'

MOVIES_TO_CHOOSE_FROM = [
    "Toy Story (1995)",
    "Jumanji (1995)",
    "Grumpier Old Men (1995)",
    "Waiting to Exhale (1995)",
    "Father of the Bride Part II(1995)",
    "Heat(1995)",
    "Sabrina(1995)",
    "Tom and Huck(1995)",
    "Sudden Death(1995)",
    "GoldenEye(1995)"
]
