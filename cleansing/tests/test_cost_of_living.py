import os
from pathlib import Path
from pprint import pprint
import json
from cleansing import cost_of_living
from collection.cost_of_living import CostOfLivingTask


def test_cost_of_living():
    CostOfLivingTask().run()
    cost_of_living.cleanse()
    output = Path(os.getenv("DATA_DIR")) / "cost_of_living_cleansed.json"
    pprint(json.load(output.open())[:5])
    assert output.exists()
