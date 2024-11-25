import os
import json
from pathlib import Path
from pprint import pprint
from collection.task import Task


def run_and_check_output(task_class: Task, output_name: str):
    task_class().run()
    output = Path(os.getenv("DATA_DIR")) / output_name
    pprint(json.load(output.open())[:2])
    assert output.exists()
