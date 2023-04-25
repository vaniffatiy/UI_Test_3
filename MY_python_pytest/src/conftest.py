import pytest
from UI_test.UI_Test_3.MY_python_pytest.src.common.webdriver_handler import WebDriverHandler


@pytest.fixture(scope="function")
def webdriver_handler():
    webdriver=WebDriverHandler()
    webdriver.setup()
    yield webdriver
    webdriver.quit()
