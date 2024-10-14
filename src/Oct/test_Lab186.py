import allure
import pytest
import requests

def test_selenium(launch_browser, close_browser): #make them part of conftest, so that can accessible here
    launch_browser
    print("Do TC")
    close_browser

