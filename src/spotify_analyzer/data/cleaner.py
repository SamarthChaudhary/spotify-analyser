import pandas as pd
import numpy as np


class DataCleaner:
    """Clean and standardize Spotify datasets."""

    def clean(self, df):
        cleaned = df.copy()

        cleaned = self._clean_column_names(cleaned)
        cleaned = self._remove_duplicates(cleaned)
        cleaned = self._clean_strings(cleaned)
        cleaned = self._convert_numeric_columns(cleaned)
        cleaned = self._handle_missing_values(cleaned)

        return cleaned

    @staticmethod
    def _clean_column_names(df):
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_", regex=False)
        )

        return df

    @staticmethod
    def _remove_duplicates(df):
        if "track_id" in df.columns:
            df = df.drop_duplicates(subset=["track_id"])
        else:
            df = df.drop_duplicates()

        return df

    @staticmethod
    def _clean_strings(df):
        string_columns = df.select_dtypes(
            include=["object", "string"]
        ).columns

        for column in string_columns:
            df[column] = (
                df[column]
                .astype("string")
                .str.strip()
            )

        return df

    @staticmethod
    def _convert_numeric_columns(df):
        numeric_columns = [
            "popularity",
            "duration_ms",
            "danceability",
            "energy",
            "key",
            "loudness",
            "mode",
            "speechiness",
            "acousticness",
            "instrumentalness",
            "liveness",
            "valence",
            "tempo",
            "time_signature",
        ]

        for column in numeric_columns:
            if column in df.columns:
                df[column] = pd.to_numeric(
                    df[column],
                    errors="coerce",
                )

        return df

    @staticmethod
    def _handle_missing_values(df):
        numeric_columns = df.select_dtypes(
            include=[np.number]
        ).columns

        for column in numeric_columns:
            df[column] = df[column].fillna(
                df[column].median()
            )

        string_columns = df.select_dtypes(
            include=["object", "string"]
        ).columns

        for column in string_columns:
            df[column] = (
                df[column]
                .fillna("Unknown")
                .astype("string")
            )

        return df