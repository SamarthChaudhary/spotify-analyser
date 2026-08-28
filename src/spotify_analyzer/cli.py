from pathlib import Path

from spotify_analyzer.data.loader import DataLoader
from spotify_analyzer.data.cleaner import DataCleaner
from spotify_analyzer.data.transformer import DataTransformer

from spotify_analyzer.analysis.overview import OverviewAnalyzer
from spotify_analyzer.analysis.artists import ArtistAnalyzer
from spotify_analyzer.analysis.genres import GenreAnalyzer
from spotify_analyzer.analysis.audio_features import (
    AudioFeatureAnalyzer,
)
from spotify_analyzer.analysis.diversity import DiversityAnalyzer

from spotify_analyzer.visualization.charts import (
    SpotifyVisualizer,
)


class SpotifyCLI:

    def __init__(self):
        self.loader = DataLoader()
        self.cleaner = DataCleaner()
        self.transformer = DataTransformer()

        self.df = None

    def load_dataset(self):
        path = input(
            "\nEnter dataset path: "
        ).strip()

        self.df = self.loader.load(path)
        self.df = self.cleaner.clean(self.df)
        self.df = self.transformer.transform(self.df)

        print(
            f"\nLoaded {len(self.df):,} tracks successfully."
        )

    def overview(self):
        analyzer = OverviewAnalyzer(self.df)
        result = analyzer.summary()

        print("\n========== OVERVIEW ==========")

        for key, value in result.items():
            if isinstance(value, float):
                print(
                    f"{key.replace('_', ' ').title()}: "
                    f"{value:.2f}"
                )
            else:
                print(
                    f"{key.replace('_', ' ').title()}: "
                    f"{value}"
                )

    def artists(self):
        analyzer = ArtistAnalyzer(self.df)

        print("\n========== TOP ARTISTS ==========")
        print(analyzer.top_artists(15))

        print(
            "\n========== MOST POPULAR ARTISTS =========="
        )

        print(
            analyzer.most_popular_artists(15)
        )

    def genres(self):
        analyzer = GenreAnalyzer(self.df)

        print("\n========== TOP GENRES ==========")
        print(analyzer.top_genres(15))

    def audio_features(self):
        analyzer = AudioFeatureAnalyzer(self.df)

        print(
            "\n========== AUDIO FEATURES =========="
        )

        print(
            analyzer.averages().round(3)
        )

        print(
            "\n========== CORRELATIONS =========="
        )

        print(
            analyzer.correlation_matrix()
            .round(2)
        )

    def diversity(self):
        analyzer = DiversityAnalyzer(self.df)

        print("\n========== DIVERSITY ==========")

        print(
            f"Genre diversity: "
            f"{analyzer.normalized_genre_diversity():.2f}/100"
        )

        print(
            f"Artist diversity: "
            f"{analyzer.normalized_artist_diversity():.2f}/100"
        )

    def visualizations(self):
        visualizer = SpotifyVisualizer()

        artist_analyzer = ArtistAnalyzer(self.df)
        genre_analyzer = GenreAnalyzer(self.df)
        audio_analyzer = AudioFeatureAnalyzer(self.df)

        visualizer.top_artists(
            artist_analyzer.top_artists(10)
        )

        visualizer.top_genres(
            genre_analyzer.top_genres(10)
        )

        visualizer.distribution(
            self.df,
            "energy",
        )

        visualizer.distribution(
            self.df,
            "danceability",
        )

        visualizer.scatter(
            self.df,
            "energy",
            "valence",
        )

        visualizer.correlation_heatmap(
            audio_analyzer.correlation_matrix()
        )

        print(
            "\nVisualizations saved to outputs/"
        )

    def menu(self):
        while True:
            print(
                """
╔══════════════════════════════════════╗
║          SPOTIFY ANALYZER            ║
╠══════════════════════════════════════╣
║ 1. Load Dataset                      ║
║ 2. Dataset Overview                  ║
║ 3. Artist Analysis                  ║
║ 4. Genre Analysis                   ║
║ 5. Audio Feature Analysis           ║
║ 6. Diversity Analysis               ║
║ 7. Generate Visualizations          ║
║ 0. Exit                              ║
╚══════════════════════════════════════╝
"""
            )

            choice = input("Select option: ").strip()

            try:
                if choice == "1":
                    self.load_dataset()

                elif self.df is None:
                    print(
                        "\nPlease load a dataset first."
                    )

                elif choice == "2":
                    self.overview()

                elif choice == "3":
                    self.artists()

                elif choice == "4":
                    self.genres()

                elif choice == "5":
                    self.audio_features()

                elif choice == "6":
                    self.diversity()

                elif choice == "7":
                    self.visualizations()

                elif choice == "0":
                    print("\nGoodbye!")
                    break

                else:
                    print("\nInvalid option.")

            except Exception as error:
                print(
                    f"\nError: {error}"
                )


def main():
    SpotifyCLI().menu()


if __name__ == "__main__":
    main()