import pandas as pd
from collection.task import Task
from collection.cleanse.cleanse_utils import filter_by_country
from utils.utils import get_data_dir, df_to_json


class QualityOfLifeTask(Task):
    output_path = "cleanse/quality_of_life.json"

    def extract(self) -> pd.DataFrame:
        return pd.read_json(get_data_dir() / "raw/quality_of_life.json")

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df["city"] = df["city"].str.lower()
        df["country"] = df["country"].str.lower()
        df["feature"] = df["feature"].str.lower()

        df = filter_by_country(df)

        return df

    def load(self, df: pd.DataFrame) -> pd.DataFrame:
        df_to_json(df, self.output_path)


if __name__ == "__main__":
    task = QualityOfLifeTask()
    task.run()
