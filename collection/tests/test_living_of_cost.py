from collection.cost_of_living import CostOfLivingTask
from tests.test_lib import run_and_check_output


def test_cost_of_living():
    run_and_check_output(CostOfLivingTask, "cost_of_living.json")
