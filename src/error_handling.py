import logging
import requests

#task 5
def test_api_with_error_handling(country_name):
    try:
        response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
        response.raise_for_status()
        # print(f"Response received for {country_name}")
        logging.warning(f"Response received for {country_name}")
        
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logging.error(f"An error occurred: {err}")

test_api_with_error_handling("xyz")
test_api_with_error_handling("USA")
test_api_with_error_handling("INDIA")
