import pandas as pd

from spotify_analyzer.data.cleaner import DataCleaner


def test_cleaner_removes_duplicates():

    df = pd.DataFrame({
        "track_id": ["1", "1"],
        "track_name": ["Song", "Song"],
        "artists": ["Artist", "Artist"],
        "popularity": [50, 50],
    })

    cleaner = DataCleaner()

    result = cleaner.clean(df)

    assert len(result) == 1


def test_cleaner_converts_numeric_values():

    df = pd.DataFrame({
        "track_id": ["1"],
        "track_name": ["Song"],
        "artists": ["Artist"],
        "popularity": ["50"],
    })

    result = DataCleaner().clean(df)

    assert result["popularity"].dtype != object