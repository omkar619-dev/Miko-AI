import unittest

import requests

# task 6

class TestRestCountriesAPI(unittest.TestCase):
    
    def test_valid_country(self):
        self.assertEqual(requests.get("https://restcountries.com/v3.1/name/India").status_code, 200)
    
    def test_invalid_country(self):
        self.assertEqual(requests.get("https://restcountries.com/v3.1/name/xyz").status_code, 404)

if __name__ == "__main__":
    unittest.main()
