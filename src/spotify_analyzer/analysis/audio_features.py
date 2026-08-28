import numpy as np

from spotify_analyzer.utils.constants import AUDIO_FEATURES


class AudioFeatureAnalyzer:

    def __init__(self, df):
        self.df = df

    def averages(self):
        available = [
            feature
            for feature in AUDIO_FEATURES
            if feature in self.df.columns
        ]

        return self.df[available].mean()

    def medians(self):
        available = [
            feature
            for feature in AUDIO_FEATURES
            if feature in self.df.columns
        ]

        return self.df[available].median()

    def standard_deviations(self):
        available = [
            feature
            for feature in AUDIO_FEATURES
            if feature in self.df.columns
        ]

        return self.df[available].std()

    def normalize_features(self):
        available = [
            feature
            for feature in AUDIO_FEATURES
            if feature in self.df.columns
        ]

        result = self.df[available].copy()

        for column in available:
            minimum = result[column].min()
            maximum = result[column].max()

            if maximum != minimum:
                result[column] = (
                    result[column] - minimum
                ) / (maximum - minimum)

        return result

    def correlation_matrix(self):
        available = [
            feature
            for feature in AUDIO_FEATURES + ["popularity"]
            if feature in self.df.columns
        ]

        return self.df[available].corr()

    def percentile(self, feature, percentile):
        if feature not in self.df.columns:
            raise ValueError(f"Unknown feature: {feature}")

        return np.percentile(
            self.df[feature].dropna(),
            percentile,
        )