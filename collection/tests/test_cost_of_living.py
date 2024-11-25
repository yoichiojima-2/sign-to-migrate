import os
import pandas as pd
from collection.cost_of_living import CostOfLivingTask
from tests.test_lib import run_and_check_output


def test_cost_of_living():
    run_and_check_output(CostOfLivingTask, CostOfLivingTask.output_name)
    df = pd.read_json(f"{os.getenv('DATA_DIR')}/{CostOfLivingTask.output_name}")
    assert set(CostOfLivingTask.cities) == set(df["city"].drop_duplicates().values)
