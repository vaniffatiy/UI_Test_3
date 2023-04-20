import pytest
from UI_test.UI_Test_3.MY_python_pytest.src.common.test_data_handler import TestDataHandler
from UI_test.UI_Test_3.MY_python_pytest.src.common.webdriver_handler import WebDriverHandler


@pytest.fixture(scope="session")
def test_data_handler():
    return TestDataHandler()


@pytest.fixture(scope="function")
def webdriver_handler():
    """
    function scope - fixture is destroyed after each test
    :return:
    """
    webdriver=WebDriverHandler()
    webdriver.setup()
    yield webdriver # test is executed here
    webdriver.quit()
