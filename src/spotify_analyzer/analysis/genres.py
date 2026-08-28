class GenreAnalyzer:

    def __init__(self, df):
        self.df = df

    def top_genres(self, n=10):
        return (
            self.df["track_genre"]
            .value_counts()
            .head(n)
        )

    def genre_statistics(self):
        features = [
            "popularity",
            "danceability",
            "energy",
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
            if feature in self.df.columns
        ]

        return (
            self.df
            .groupby("track_genre")[available]
            .mean()
            .sort_values(
                "popularity",
                ascending=False,
            )
        )

    def compare_genres(self, genre_a, genre_b):
        stats = self.genre_statistics()

        if genre_a not in stats.index:
            raise ValueError(f"Unknown genre: {genre_a}")

        if genre_b not in stats.index:
            raise ValueError(f"Unknown genre: {genre_b}")

        return stats.loc[[genre_a, genre_b]]