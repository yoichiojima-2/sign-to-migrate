from collection.happiness import HappinessTask
from tests.test_lib import run_and_check_output


def test_happiness():
    run_and_check_output(HappinessTask, HappinessTask.output_name)
