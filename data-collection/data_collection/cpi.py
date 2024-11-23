import os
import requests
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
from task import Task


class CpiTask(Task):
    load_dotenv()

    def extract(self) -> pd.DataFrame:
        response = requests.get(
            "https://api.worldbank.org/v2/country/all/indicator/FP.CPI.TOTL",
            params={
                "format": "json",
                "date": "2010:2024",
                "per_page": 10000,
            },
        )
        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data[1])
        else:
            raise RuntimeError(f"Failed to fetch data: {response.status_code}")

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df[pd.notna(df["value"])].copy()
        df["country_name"] = df["country"].apply(lambda x: x["value"])
        df["country_id"] = df["country"].apply(lambda x: x["id"])
        df = df[["countryiso3code", "country_name", "date", "value"]]
        return df

    def load(self, df: pd.DataFrame) -> None:
        df.to_json(Path(os.getenv("DATA_DIR")) / "cpi.json", orient="records")