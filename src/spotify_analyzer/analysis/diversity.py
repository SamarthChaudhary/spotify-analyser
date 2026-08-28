import numpy as np


class DiversityAnalyzer:

    def __init__(self, df):
        self.df = df

    @staticmethod
    def entropy(series):
        probabilities = (
            series.value_counts(normalize=True)
        )

        return -np.sum(
            probabilities *
            np.log2(probabilities)
        )

    def genre_entropy(self):
        return self.entropy(
            self.df["track_genre"]
        )

    def artist_entropy(self):
        return self.entropy(
            self.df["artists"]
        )

    def normalized_genre_diversity(self):
        counts = self.df["track_genre"].value_counts()

        entropy = self.entropy(
            self.df["track_genre"]
        )

        maximum = np.log2(len(counts))

        if maximum == 0:
            return 0

        return entropy / maximum * 100

    def normalized_artist_diversity(self):
        counts = self.df["artists"].value_counts()

        entropy = self.entropy(
            self.df["artists"]
        )

        maximum = np.log2(len(counts))

        if maximum == 0:
            return 0

        return entropy / maximum * 100