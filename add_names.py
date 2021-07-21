import pandas as pd
import os
import names
from pandas.core import series

MAIN_DIR = os.path.dirname(os.path.abspath(__file__))


def givename(x):
    name = names.get_full_name()
    return name


ratings_csv = pd.read_csv(os.path.join(MAIN_DIR, 'static/data/ratings.csv'))


userIds = ratings_csv['userId'].unique()
namesList = [names.get_full_name() for _ in userIds]
user_series = pd.Series(namesList, index=userIds, name="name")

df = pd.merge(ratings_csv, user_series, left_on='userId',
              right_index=True, how='outer')

df.to_csv("ratings_names.csv")
