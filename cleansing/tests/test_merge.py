import os
from pathlib import Path
from pprint import pprint
import json
from cleansing.merge import merge


def test_cost_of_living():
    merge()
    output = Path(os.getenv("DATA_DIR")) / "merged.json"
    pprint(json.load(output.open())[:5])
    assert output.exists()
