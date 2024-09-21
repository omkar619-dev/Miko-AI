from src.test_case_design import test_country_api


def test_country_api_parameterized(country_name):
    test_country_api(country_name)

