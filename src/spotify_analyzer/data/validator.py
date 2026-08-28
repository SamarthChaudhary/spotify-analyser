import pandas as pd

from spotify_analyzer.utils.constants import (
    TRACK_COLUMNS,
    REQUIRED_TRACK_COLUMNS,
)


class DataValidator:
    """Validate Spotify dataset structure and values."""

    def validate_columns(self, df):
        missing = [
            column
            for column in REQUIRED_TRACK_COLUMNS
            if column not in df.columns
        ]

        return {
            "valid": len(missing) == 0,
            "missing_columns": missing,
        }

    def validate(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame.")

        result = self.validate_columns(df)

        errors = []

        if not result["valid"]:
            errors.append(
                f"Missing required columns: {result['missing_columns']}"
            )

        if "popularity" in df.columns:
            invalid = df[
                (df["popularity"] < 0) |
                (df["popularity"] > 100)
            ]

            if not invalid.empty:
                errors.append(
                    f"Found {len(invalid)} rows with invalid popularity."
                )

        bounded_features = [
            "danceability",
            "energy",
            "speechiness",
            "acousticness",
            "instrumentalness",
            "liveness",
            "valence",
        ]

        for column in bounded_features:
            if column in df.columns:
                invalid = df[
                    (df[column] < 0) |
                    (df[column] > 1)
                ]

                if not invalid.empty:
                    errors.append(
                        f"{column}: {len(invalid)} invalid values."
                    )

        return {
            "valid": len(errors) == 0,
            "errors": errors,
        }