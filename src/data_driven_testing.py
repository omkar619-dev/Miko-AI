import csv
import logging
from src.test_case_design import test_country_api

def load_test_data(file_name):
    test_data = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            test_data.append(row)
    return test_data

def test_with_data(file_name):
    data = load_test_data(file_name)
    for country in data:
        try:
            print(country[0])
            test_country_api(country[0])
            
        except Exception:
            logging.error(f"Failed test for country: {country[0]}")



