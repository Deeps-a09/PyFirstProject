import pytest
import allure

@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.smoke

def test_verify_sub0():
    assert 2 - 2 == 0
@pytest.mark.smoke
def test_verify_sub1():
    assert 3 + 3 == 0
@pytest.mark.smoke
def test_verify_sub2():
    assert 1 - 1 == 0
@pytest.mark.regression
def test_verify_sub3():
    assert 1 - 1 == 1

@pytest.mark.skip(reason="NA")
def test_verify_sub4():
    assert 0 - 0 != 0


# -m use for marking
# in terminal we will write pytest -m "smoke" (full path)

# for allure - write in terminal --> pytest -m "smoke" src/Oct/test_Lab176.py --alluredir=allure_result
# for HTMl allure report type- allure serve allure_result

# HTML allure report-- type in terminal-> allure serve allure_result