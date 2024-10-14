import allure
import pytest
import requests

#PUT Req
def test_update_req_1(create_token,create_booking):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking)
    PUT_URL = base_url + base_path
    cookie = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    json_payload = {
        "firstname": "Jimny",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    # Status Code
    assert response.status_code == 200

    responseData = response.json()
    print(responseData)
    assert responseData["firstname"] == "Jimny"