import requests
import logging
import json
import csv

# Configuring logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_country_api(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    logging.info(f"Sending GET request to {url}")
    response = requests.get(url)
    
    try:
        # Positive assertion
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        logging.info(f"Response: {json.dumps(data, indent=4)}")
        assert "name" in data[0] and "capital" in data[0], "Missing required fields in response"
        logging.info(f"Test passed for country: {country_name}")
    except AssertionError as e:
        logging.error(f"Test failed: {e}")
        raise

def test_invalid_country_api(invalid_country_name):
    url = f"https://restcountries.com/v3.1/name/{invalid_country_name}"
    logging.info(f"Sending GET request to {url}")
    response = requests.get(url)
    
    try:
        # Negative assertion
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
        logging.info(f"Test passed for invalid country: {invalid_country_name}")
    except AssertionError as e:
        logging.error(f"Test failed: {e}")
        raise
# test_country_api("India")
# test_country_api("eesti")
test_invalid_country_api("xyz")