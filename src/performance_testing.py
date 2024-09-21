import logging
import time

import requests

def test_performance(country_name):
    start_time = time.time()
    response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
    response_time = time.time() - start_time
    logging.info(f"Response time for {country_name}: {response_time:.2f} seconds")
