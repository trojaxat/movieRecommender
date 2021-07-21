import pandas as pd


class DataFrame:

    def __init__(self, dataframe):
        self.df = dataframe

    def cleanData(self, df=None, fill=True):
        """ 
        - fillnas using mean
        """
        if df is not None:
            df = self.df

        df = pd.pivot_table(
            df, values='rating', index='userId', columns='movieId')

        if fill is True:
            df = df.fillna(df.mean().mean())

        df = pd.DataFrame(df, index=df.index, columns=df.columns).values
        return df
