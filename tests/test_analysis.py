import pandas as pd

from spotify_analyzer.analysis.overview import (
    OverviewAnalyzer,
)

from spotify_analyzer.analysis.artists import (
    ArtistAnalyzer,
)


def create_dataframe():

    return pd.DataFrame({
        "track_name": [
            "Song 1",
            "Song 2",
            "Song 3",
        ],
        "artists": [
            "Artist A",
            "Artist A",
            "Artist B",
        ],
        "album_name": [
            "Album A",
            "Album A",
            "Album B",
        ],
        "popularity": [
            50,
            70,
            80,
        ],
        "track_genre": [
            "pop",
            "pop",
            "rock",
        ],
        "duration_minutes": [
            3,
            4,
            5,
        ],
    })


def test_overview():

    df = create_dataframe()

    analyzer = OverviewAnalyzer(df)

    result = analyzer.summary()

    assert result["tracks"] == 3
    assert result["artists"] == 2
    assert result["albums"] == 2
    assert result["genres"] == 2


def test_top_artists():

    df = create_dataframe()

    result = ArtistAnalyzer(
        df
    ).top_artists(1)

    assert result.index[0] == "Artist A"
    assert result.iloc[0] == 2