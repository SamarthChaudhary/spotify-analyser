class ArtistAnalyzer:

    def __init__(self, df):
        self.df = df

    def top_artists(self, n=10):
        return (
            self.df["artists"]
            .value_counts()
            .head(n)
        )

    def most_popular_artists(self, n=10, min_tracks=3):
        result = (
            self.df
            .groupby("artists")
            .agg(
                average_popularity=("popularity", "mean"),
                track_count=("track_name", "count"),
            )
        )

        result = result[
            result["track_count"] >= min_tracks
        ]

        return result.sort_values(
            "average_popularity",
            ascending=False,
        ).head(n)

    def artist_audio_profile(self, artist):
        artist_df = self.df[
            self.df["artists"].str.contains(
                artist,
                case=False,
                na=False,
            )
        ]

        if artist_df.empty:
            return None

        audio_columns = [
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
            column
            for column in audio_columns
            if column in artist_df.columns
        ]

        return artist_df[available].mean()