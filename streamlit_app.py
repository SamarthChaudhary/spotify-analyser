import tempfile

import pandas as pd
import streamlit as st

from src.spotify_analyzer.app import SpotifyAnalyzer

from src.spotify_analyzer.analysis.overview import (
    OverviewAnalyzer,
)

from src.spotify_analyzer.analysis.artists import (
    ArtistAnalyzer,
)

from src.spotify_analyzer.analysis.genres import (
    GenreAnalyzer,
)

from src.spotify_analyzer.analysis.audio_features import (
    AudioFeatureAnalyzer,
)

from src.spotify_analyzer.analysis.diversity import (
    DiversityAnalyzer,
)

from src.spotify_analyzer.visualization.charts import (
    SpotifyVisualizer,
)


st.set_page_config(
    page_title="Spotify Analyzer",
    page_icon="🎵",
    layout="wide",
)


st.title("🎵 Spotify Analyzer")

st.markdown(
    """
Analyze Spotify datasets using Python, Pandas,
NumPy and data visualization.
"""
)


uploaded_file = st.file_uploader(
    "Upload your Spotify dataset",
    type=["csv", "json"],
)


@st.cache_data
def process_dataframe(df):
    analyzer = SpotifyAnalyzer()
    return analyzer.load_dataframe(df)


if uploaded_file is not None:

    try:
        if uploaded_file.name.endswith(".csv"):
            raw_df = pd.read_csv(
                uploaded_file
            )

        else:
            raw_df = pd.read_json(
                uploaded_file
            )

        df = process_dataframe(raw_df)

        st.success(
            f"Successfully loaded {len(df):,} tracks."
        )

        overview = OverviewAnalyzer(df)
        artist_analysis = ArtistAnalyzer(df)
        genre_analysis = GenreAnalyzer(df)
        audio_analysis = AudioFeatureAnalyzer(df)
        diversity = DiversityAnalyzer(df)

        summary = overview.summary()

        st.header("Dataset Overview")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Tracks",
            f"{summary['tracks']:,}",
        )

        col2.metric(
            "Artists",
            f"{summary['artists']:,}",
        )

        col3.metric(
            "Albums",
            f"{summary['albums']:,}",
        )

        col4.metric(
            "Genres",
            f"{summary['genres']:,}",
        )

        st.divider()

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "Artists",
                "Genres",
                "Audio",
                "Correlations",
                "Diversity",
            ]
        )

        with tab1:
            st.subheader("Top Artists")

            st.bar_chart(
                artist_analysis
                .top_artists(15)
            )

            st.subheader(
                "Most Popular Artists"
            )

            st.dataframe(
                artist_analysis
                .most_popular_artists(15)
            )

        with tab2:
            st.subheader("Top Genres")

            st.bar_chart(
                genre_analysis
                .top_genres(15)
            )

            st.subheader(
                "Genre Statistics"
            )

            st.dataframe(
                genre_analysis
                .genre_statistics()
            )

        with tab3:
            st.subheader(
                "Average Audio Features"
            )

            averages = (
                audio_analysis
                .averages()
            )

            st.bar_chart(
                averages
            )

            feature = st.selectbox(
                "Choose feature",
                [
                    "energy",
                    "danceability",
                    "valence",
                    "acousticness",
                    "instrumentalness",
                    "speechiness",
                    "liveness",
                    "tempo",
                    "loudness",
                ],
            )

            st.subheader(
                f"{feature.title()} Distribution"
            )

            st.line_chart(
                df[feature]
                .value_counts()
                .sort_index()
            )

        with tab4:
            st.subheader(
                "Audio Feature Correlation"
            )

            st.dataframe(
                audio_analysis
                .correlation_matrix()
                .round(2)
            )

        with tab5:
            genre_score = (
                diversity
                .normalized_genre_diversity()
            )

            artist_score = (
                diversity
                .normalized_artist_diversity()
            )

            col1, col2 = st.columns(2)

            col1.metric(
                "Genre Diversity",
                f"{genre_score:.1f}/100",
            )

            col2.metric(
                "Artist Diversity",
                f"{artist_score:.1f}/100",
            )

        st.divider()

        st.subheader(
            "Explore Raw Data"
        )

        st.dataframe(
            df.head(100),
            use_container_width=True,
        )

    except Exception as error:
        st.error(
            f"Could not process dataset: {error}"
        )

else:

    st.info(
        "Upload a Spotify CSV or JSON dataset to begin."
    )

    st.markdown(
        """
### What you can analyze

- 🎤 Artists
- 🎼 Genres
- 🔊 Audio features
- 📊 Popularity
- 📈 Correlations
- 🧮 Statistics
- 🧭 Genre diversity
- 🎧 Artist diversity
- 📉 Distributions
"""
    )