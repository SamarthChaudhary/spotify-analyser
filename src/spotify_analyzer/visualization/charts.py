from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


class SpotifyVisualizer:

    def __init__(self, output_dir="outputs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save_figure(self, filename):
        path = self.output_dir / filename
        plt.tight_layout()
        plt.savefig(path, dpi=150)
        plt.close()

        return path

    def top_artists(self, series, n=10):
        plt.figure(figsize=(10, 6))

        series.head(n).sort_values().plot(
            kind="barh"
        )

        plt.title("Top Artists")
        plt.xlabel("Number of Tracks")
        plt.ylabel("Artist")

        return self.save_figure(
            "top_artists.png"
        )

    def top_genres(self, series, n=10):
        plt.figure(figsize=(10, 6))

        series.head(n).sort_values().plot(
            kind="barh"
        )

        plt.title("Top Genres")
        plt.xlabel("Number of Tracks")
        plt.ylabel("Genre")

        return self.save_figure(
            "top_genres.png"
        )

    def distribution(self, df, feature):
        plt.figure(figsize=(10, 6))

        sns.histplot(
            data=df,
            x=feature,
            kde=True,
        )

        plt.title(
            f"Distribution of {feature.title()}"
        )

        return self.save_figure(
            f"{feature}_distribution.png"
        )

    def scatter(self, df, x, y):
        plt.figure(figsize=(10, 6))

        sns.scatterplot(
            data=df,
            x=x,
            y=y,
            alpha=0.4,
        )

        plt.title(
            f"{x.title()} vs {y.title()}"
        )

        return self.save_figure(
            f"{x}_vs_{y}.png"
        )

    def correlation_heatmap(self, correlation):
        plt.figure(figsize=(12, 9))

        sns.heatmap(
            correlation,
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            center=0,
        )

        plt.title("Audio Feature Correlation")

        return self.save_figure(
            "correlation_heatmap.png"
        )

    def genre_boxplot(self, df, feature, top_n=10):
        top_genres = (
            df["track_genre"]
            .value_counts()
            .head(top_n)
            .index
        )

        filtered = df[
            df["track_genre"].isin(top_genres)
        ]

        plt.figure(figsize=(14, 7))

        sns.boxplot(
            data=filtered,
            x="track_genre",
            y=feature,
        )

        plt.xticks(rotation=45)
        plt.title(
            f"{feature.title()} by Genre"
        )

        return self.save_figure(
            f"{feature}_by_genre.png"
        )