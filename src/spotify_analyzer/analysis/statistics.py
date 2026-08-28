import numpy as np


class StatisticalAnalyzer:

    def __init__(self, df):
        self.df = df

    def describe(self):
        return self.df.describe()

    def feature_statistics(self, feature):
        if feature not in self.df.columns:
            raise ValueError(f"Unknown feature: {feature}")

        values = self.df[feature].dropna().to_numpy()

        return {
            "mean": np.mean(values),
            "median": np.median(values),
            "std": np.std(values),
            "min": np.min(values),
            "max": np.max(values),
            "q25": np.percentile(values, 25),
            "q75": np.percentile(values, 75),
        }

    def correlation(self, feature_a, feature_b):
        if feature_a not in self.df.columns:
            raise ValueError(feature_a)

        if feature_b not in self.df.columns:
            raise ValueError(feature_b)

        valid = self.df[
            [feature_a, feature_b]
        ].dropna()

        return np.corrcoef(
            valid[feature_a],
            valid[feature_b],
        )[0, 1]