import pandas as pd

from spotify_analyzer.data.validator import (
    DataValidator,
)


def test_valid_dataset():

    df = pd.DataFrame({
        "track_name": ["Song"],
        "artists": ["Artist"],
        "popularity": [50],
    })

    result = DataValidator().validate(df)

    assert result["valid"] is True


def test_missing_required_column():

    df = pd.DataFrame({
        "track_name": ["Song"],
        "popularity": [50],
    })

    result = DataValidator().validate(df)

    assert result["valid"] is False