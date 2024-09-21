from src.data_driven_testing import test_with_data
from src.test_case_design import test_country_api,test_invalid_country_api
from src.performance_testing import test_performance
from src.parametrization import test_country_api_parameterized

if __name__ == "__main__":
    
    test_country_api("India")  #task 1
    test_country_api("eesti")  #task 1
    test_invalid_country_api("notacountry")  #task 1
    test_with_data("countries.csv")   #task 2
    test_performance("USA")  #task 7
    
    countries = ["India", "USA", "Germany"]
    for country in countries:
        test_country_api_parameterized(country)    #task 3