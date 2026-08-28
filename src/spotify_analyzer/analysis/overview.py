class OverviewAnalyzer:

    def __init__(self, df):
        self.df = df

    def total_tracks(self):
        return len(self.df)

    def total_artists(self):
        if "artists" not in self.df:
            return 0

        return self.df["artists"].nunique()

    def total_albums(self):
        if "album_name" not in self.df:
            return 0

        return self.df["album_name"].nunique()

    def total_genres(self):
        if "track_genre" not in self.df:
            return 0

        return self.df["track_genre"].nunique()

    def average_popularity(self):
        return self.df["popularity"].mean()

    def average_duration(self):
        if "duration_minutes" in self.df:
            return self.df["duration_minutes"].mean()

        return None

    def summary(self):
        return {
            "tracks": self.total_tracks(),
            "artists": self.total_artists(),
            "albums": self.total_albums(),
            "genres": self.total_genres(),
            "average_popularity": self.average_popularity(),
            "average_duration_minutes": self.average_duration(),
        }