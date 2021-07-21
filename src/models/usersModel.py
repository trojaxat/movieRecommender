from src.models.dataframeModel import DataFrame
from src.models.userModel import User
from IPython.display import display


class Users(DataFrame):
    """Class for users"""

    def __init__(self, df):
        super().__init__(df)

    def getUsersWithMostRatings(self, amount):
        users = self.df.groupby('userId')['movieId'].nunique(
        ).sort_values(ascending=False).reset_index(name='count')
        userIds = users['userId'].head(amount)
        userList = self.createUsersList(userIds)
        return userList

    def createUsersList(self, ids):
        userList = []
        for id in ids:
            ratings = self.getRatingsAmount(id)
            name = self.getUserName(id)
            user = User(id, name, ratings)
            userList.append(user)
        return userList

    def getUserName(self, id):
        return str(self.df.loc[self.df['userId'] == id]['name'].iloc[0])

    def getRatingsAmount(self, id):
        display(self.df)
        return self.df[self.df['userId'] == id]['movieId'].value_counts().sum()
