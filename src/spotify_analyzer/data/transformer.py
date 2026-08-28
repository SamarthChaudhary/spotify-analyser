import numpy as np


class DataTransformer:
    """Create derived features for analysis."""

    def transform(self, df):
        transformed = df.copy()

        transformed = self.add_duration_features(transformed)
        transformed = self.add_energy_category(transformed)
        transformed = self.add_mood_category(transformed)

        return transformed

    @staticmethod
    def add_duration_features(df):
        if "duration_ms" in df.columns:
            df["duration_seconds"] = df["duration_ms"] / 1000
            df["duration_minutes"] = df["duration_ms"] / 60000

        return df

    @staticmethod
    def add_energy_category(df):
        if "energy" not in df.columns:
            return df

        df["energy_category"] = np.select(
            [
                df["energy"] < 0.3,
                df["energy"] < 0.7,
                df["energy"] >= 0.7,
            ],
            [
                "Low",
                "Medium",
                "High",
            ],
            default="Unknown",
        )

        return df

    @staticmethod
    def add_mood_category(df):
        if not {"energy", "valence"}.issubset(df.columns):
            return df

        conditions = [
            (df["energy"] >= 0.7) & (df["valence"] >= 0.6),
            (df["energy"] < 0.4) & (df["valence"] < 0.4),
            (df["energy"] >= 0.7) & (df["valence"] < 0.4),
            (df["energy"] < 0.4) & (df["valence"] >= 0.6),
        ]

        choices = [
            "Happy / Energetic",
            "Melancholic",
            "Intense",
            "Calm / Positive",
        ]

        df["mood_category"] = np.select(
            conditions,
            choices,
            default="Balanced",
        )

        return df