from pathlib import Path
import luigi
from collection.main import Weather
from utils.utils import get_data_dir


def test_cost_of_living():
    luigi.build([Weather()], local_scheduler=True)
    assert Path(get_data_dir() / Weather().output().path).exists()