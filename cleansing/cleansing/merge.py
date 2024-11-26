import os
from pathlib import Path
import pandas as pd


def merge():
    output_name = "merged.json"
    cost_df = pd.read_json(f"{os.getenv('DATA_DIR')}/cost_of_living_cleansed.json")
    happness_df = pd.read_json(f"{os.getenv('DATA_DIR')}/happiness.json")
    df = cost_df.merge(
        happness_df, left_on="country", right_on="Country", how="left"
    ).drop(columns=["Country"])
    df.to_json(Path(os.getenv("DATA_DIR")) / output_name, orient="records", index=False)


if __name__ == "__main__":
    merge()
