from spotify_analyzer.data.loader import DataLoader
from spotify_analyzer.data.cleaner import DataCleaner
from spotify_analyzer.data.validator import DataValidator
from spotify_analyzer.data.transformer import DataTransformer


class SpotifyAnalyzer:

    def __init__(self):
        self.loader = DataLoader()
        self.validator = DataValidator()
        self.cleaner = DataCleaner()
        self.transformer = DataTransformer()

        self.df = None

    def load(self, path):
        df = self.loader.load(path)

        validation = self.validator.validate(df)

        if not validation["valid"]:
            raise ValueError(
                "\n".join(validation["errors"])
            )

        df = self.cleaner.clean(df)
        df = self.transformer.transform(df)

        self.df = df

        return df

    def load_dataframe(self, df):
        validation = self.validator.validate(df)

        if not validation["valid"]:
            raise ValueError(
                "\n".join(validation["errors"])
            )

        df = self.cleaner.clean(df)
        df = self.transformer.transform(df)

        self.df = df

        return df