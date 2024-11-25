import os
import pandas as pd
from collection.cost_of_living import CostOfLivingTask
from tests.test_lib import run_and_check_output


def test_cost_of_living():
    output_name = "cost_of_living.json"
    run_and_check_output(CostOfLivingTask, output_name)
    df = pd.read_json(f"{os.getenv('DATA_DIR')}/{output_name}")
    print(df[["city"]].drop_duplicates().values)
    assert set(CostOfLivingTask.cities) == set(df["city"].drop_duplicates().values)
