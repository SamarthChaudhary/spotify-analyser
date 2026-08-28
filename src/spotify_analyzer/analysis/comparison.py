import pandas as pd


class DatasetComparator:

    def __init__(self, user_df, reference_df):
        self.user_df = user_df
        self.reference_df = reference_df

    def audio_comparison(self):
        features = [
            "energy",
            "danceability",
            "valence",
            "acousticness",
            "instrumentalness",
            "speechiness",
            "liveness",
            "tempo",
            "loudness",
        ]

        available = [
            feature
            for feature in features
            if feature in self.user_df.columns
            and feature in self.reference_df.columns
        ]

        user_values = self.user_df[available].mean()
        reference_values = self.reference_df[available].mean()

        result = pd.DataFrame({
            "user": user_values,
            "reference": reference_values,
        })

        result["difference"] = (
            result["user"] -
            result["reference"]
        )

        result["percentage_difference"] = (
            result["difference"] /
            result["reference"].replace(0, pd.NA)
        ) * 100

        return result

    def popularity_comparison(self):
        return {
            "user": self.user_df["popularity"].mean(),
            "reference": self.reference_df["popularity"].mean(),
        }