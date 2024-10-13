# How to create a test case in allure
# 1. import pytest
# 2. import allure
# 3. Need to write the test cases
# Then I can add marking because of grouping problem


import pytest
import allure
@allure.title("TC#1 - Verify that 2 - 2 is equal to 0")
@allure.description("This smoke test case check- Verify that 2 -2 is equal to 0")
@pytest.mark.smoke
def test_sub0():
    assert 2 - 2 == 0

@allure.title("TC#2 - Verify that 2 + 2 is equal to 4")
@allure.description("This smoke test case check- Verify that 2 + 2 is equal to 4")
@pytest.mark.smoke
def test_add0():
    assert 2 + 2 == 4

@allure.title("TC#3 - Verify that 3 - 3 is equal to 0")
@allure.description("This smoke test case check- Verify that 3 -3 is equal to 0")
@pytest.mark.regression
def test_sub1():
    assert 3 - 3 == 0

@allure.title("TC#4 - Verify that 0 - 0 is equal to 0")
@allure.description("This smoke test case check- Verify that 0 -0 is equal to 0")
@pytest.mark.smoke
def test_sub4():
    assert 0 - 0 != 0

@pytest.mark.skip(reason= "NA")
def test_sub5():
    assert 0 - 0 == 0