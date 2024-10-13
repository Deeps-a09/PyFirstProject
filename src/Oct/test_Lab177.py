# Create Booking Testcase
# Verify that booking ID  not null
# status code

# Request Moduule - requests

import pytest
import allure
import requests

@allure.title("Test GET Request - RestFUL BOOKER Project #1")
@allure.description("TC#1 -> Verify that GET Request with ID works")
@allure.tag("regression", "p0", "smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Deepshikha Arya")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_Data = requests.get(url)
    print(response_Data.text)
    print(response_Data.json())
    print(response_Data.headers)
    assert response_Data.status_code == 200

@allure.title("Test GET Request - RestFUL BOOKER Project #1")
@allure.description("TC#2 -> Verify that GET Request with ID works")
@allure.label("owner", "Deepshikha Arya")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_single_request_by_id2():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_Data = requests.get(url)
    print(response_Data.text)
    print(response_Data.json())
    print(response_Data.headers)
    assert response_Data.status_code == 404