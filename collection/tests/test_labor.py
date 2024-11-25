from collection import labor
from tests.test_lib import run_and_check_output


def test_working_poverty_rate():
    run_and_check_output(labor.WorkingPovertyRate, "working_poverty_rate.json")


def test_social_protection():
    run_and_check_output(labor.SocialProtection, "social_protection.json")


def test_women_in_senior_and_middle_position():
    run_and_check_output(labor.WomenInSeniorAndMiddlePosition, "women_in_senior_and_middle_position.json")


def test_women_in_managerial_position():
    run_and_check_output(labor.WomenInManagerialPosition, "women_in_managerial_position.json")


def test_annual_growth_rate_per_worker():
    run_and_check_output(labor.AnnualGrowthRatePerWorker, "annual_growth_rate_per_worker.json")


def test_informal_employment():
    run_and_check_output(labor.InformalEmployment, "informal_employment.json")


def test_average_hourly_earnings():
    run_and_check_output(labor.AverageHourlyEarnings, "average_hourly_earnings.json")


def test_unemployment_rate():
    run_and_check_output(labor.UnemploymentRate, "unemployment_rate.json")


def test_unemployment_rate_disability():
    run_and_check_output(labor.UnemploymentRateDisability, "unemployment_rate_disability.json")


def test_youth_neet_proportion():
    run_and_check_output(labor.YouthNeetProportion, "youth_neet_proportion.json")


def test_labour_rights():
    run_and_check_output(labor.LabourRights, "labour_rights.json")
