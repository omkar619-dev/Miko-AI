import requests
import logging

#task 4
def validate_response_structure(data):
    assert isinstance(data, list), "Response should be a list"
    logging.warning("It is a list")
    assert "name" in data[0], "Response should contain 'name'"
    logging.warning("It is a name")
    assert "capital" in data[0], "Response should contain 'capital'"
    logging.warning("It is a capital")
    assert isinstance(data[0]["population"], int), "Population should be an integer"

def test_country_api_with_validation(country_name):
    response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
    data = response.json()
    validate_response_structure(data)


test_country_api_with_validation("INDIA")