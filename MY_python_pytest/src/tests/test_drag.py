from UI_test.UI_Test_3.MY_python_pytest.src.common.webdriver_handler import WebDriverHandler
from UI_test.UI_Test_3.MY_python_pytest.src.pages.drag_page import DragPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time


class TestDynamic:

    def test_drag_drop(self, webdriver_handler):
        drag = DragPage(webdriver_handler)
        drag.open_site()
        time.sleep(15)
        drag.drag_drop()
        # drag.drag_drop_offset()










