import pandas as pd

from spotify_analyzer.analysis.statistics import (
    StatisticalAnalyzer,
)


def test_feature_statistics():

    df = pd.DataFrame({
        "energy": [0.2, 0.4, 0.6, 0.8],
    })

    analyzer = StatisticalAnalyzer(df)

    result = analyzer.feature_statistics(
        "energy"
    )

    assert result["mean"] == 0.5
    assert result["min"] == 0.2
    assert result["max"] == 0.8


def test_correlation():

    df = pd.DataFrame({
        "energy": [1, 2, 3],
        "loudness": [2, 4, 6],
    })

    analyzer = StatisticalAnalyzer(df)

    result = analyzer.correlation(
        "energy",
        "loudness",
    )

    assert round(result, 5) == 1