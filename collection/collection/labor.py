import os
import requests
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from io import StringIO
from collection.task import Task


@dataclass
class LaborTask(Task):
    name: str
    dataset_id: str
    dataset_name: str

    def extract(self) -> pd.DataFrame:
        api_url = "https://rplumber.ilo.org/data/indicator/"
        params = {
            "id": self.dataset_id,
            "lang": "en",
            "type": "label",
            "format": "csv",
            "channel": "ilostat",
            "title": self.dataset_name,
        }
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            return pd.read_csv(StringIO(response.text))
        else:
            raise RuntimeError(f"Failed to retrieve data: {response.status_code}")

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df.columns = [col.replace(".label", "") for col in df.columns]
        return df.rename(columns={"ref_area": "country", "time": "year"})

    def load(self, df: pd.DataFrame) -> pd.DataFrame:
        df.to_json(Path(os.getenv("DATA_DIR")) / f"{self.name}.json", orient="records", index=False)


class WorkingPovertyRate(LaborTask):
    def __init__(self):
        super().__init__(
            name="working_poverty_rate",
            dataset_id="SDG_0111_SEX_AGE_RT_A",
            dataset_name="sdg-indicator-111-working-poverty-rate-percentage-of-employed-living-below-us215-ppp-annual",
        )


class SocialProtection(LaborTask):
    def __init__(self):
        super().__init__(
            name="social_protection",
            dataset_id="SDG_0131_SEX_SOC_RT_A",
            dataset_name="sdg-indicator-131-proportion-of-population-covered-by-social-protection-floorssystems-annual",
        )


class WomenInSeniorAndMiddlePosition(LaborTask):
    def __init__(self):
        super().__init__(
            name="women_in_senior_and_middle_position",
            dataset_id="SDG_0552_NOC_RT_A",
            dataset_name="sdg-indicator-552-proportion-of-women-in-senior-and-middle-management-positions-annual",
        )


class WomenInManagerialPosition(LaborTask):
    def __init__(self):
        super().__init__(
            name="women_in_managerial_position",
            dataset_id="SDG_T552_NOC_RT_A",
            dataset_name="sdg-indicator-552-proportion-of-women-in-managerial-positions-annual",
        )


class AnnualGrowthRatePerWorker(LaborTask):
    def __init__(self):
        super().__init__(
            name="annual_growth_rate_per_worker",
            dataset_id="SDG_0821_NOC_RT_A",
            dataset_name="sdg-indicator-821-annual-growth-rate-of-output-per-worker-gdp-constant-2017-international-at-ppp-annual",
        )


class InformalEmployment(LaborTask):
    def __init__(self):
        super().__init__(
            name="informal_employment",
            dataset_id="SDG_0831_SEX_ECO_RT_A",
            dataset_name="sdg-indicator-831-proportion-of-informal-employment-in-total-employment-by-sex-and-sector-annual",
        )


class AverageHourlyEarnings(LaborTask):
    def __init__(self):
        super().__init__(
            name="average_hourly_earnings",
            dataset_id="SDG_0851_SEX_OCU_NB_A",
            dataset_name="sdg-indicator-851-average-hourly-earnings-of-employees-by-sex-local-currency-annual",
        )


class UnemploymentRate(LaborTask):
    def __init__(self):
        super().__init__(
            name="unemployment_rate",
            dataset_id="SDG_0852_SEX_AGE_RT_A",
            dataset_name="sdg-indicator-852-unemployment-rate-annual",
        )


class UnemploymentRateDisability(LaborTask):
    def __init__(self):
        super().__init__(
            name="unemployment_rate_disability",
            dataset_id="SDG_0852_SEX_DSB_RT_A",
            dataset_name="sdg-indicator-852-unemployment-rate-by-disability-status-annual",
        )


class YouthNeetProportion(LaborTask):
    def __init__(self):
        super().__init__(
            name="youth_neet_proportion",
            dataset_id="SDG_0861_SEX_RT_A",
            dataset_name="sdg-indicator-861-proportion-of-youth-aged-15-24-years-not-in-education-employment-or-training-annual",
        )


class LabourRights(LaborTask):
    def __init__(self):
        super().__init__(
            name="labour_rights",
            dataset_id="SDG_0882_NOC_RT_A",
            dataset_name="sdg-indicator-882-level-of-national-compliance-with-labour-rights-freedom-of-association-and-collective-bargaining-annual",
        )


if __name__ == "__main__":
    WorkingPovertyRate().run()
    SocialProtection().run()
    WomenInSeniorAndMiddlePosition().run()
    WomenInManagerialPosition().run()
    AnnualGrowthRatePerWorker().run()
    InformalEmployment().run()
    AverageHourlyEarnings().run()
    UnemploymentRate().run()
    UnemploymentRateDisability().run()
    YouthNeetProportion().run()
    LabourRights().run()
