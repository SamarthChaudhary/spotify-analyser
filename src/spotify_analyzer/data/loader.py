from pathlib import Path
import pandas as pd


class DataLoader:
    """Load Spotify datasets from supported file formats."""

    SUPPORTED_EXTENSIONS = {".csv", ".json"}

    def load(self, file_path):
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        extension = path.suffix.lower()

        if extension == ".csv":
            return self._load_csv(path)

        if extension == ".json":
            return self._load_json(path)

        raise ValueError(
            f"Unsupported file format: {extension}. "
            f"Supported formats: {self.SUPPORTED_EXTENSIONS}"
        )

    @staticmethod
    def _load_csv(path):
        return pd.read_csv(path)

    @staticmethod
    def _load_json(path):
        return pd.read_json(path)

    @staticmethod
    def load_dataframe(dataframe):
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Expected a pandas DataFrame.")

        return dataframe.copy()