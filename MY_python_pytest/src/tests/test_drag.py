from UI_test.UI_Test_3.MY_python_pytest.src.pages.drag_page import DragPage
import time


class TestDynamic:

    def test_dynamic_id(self, webdriver_handler):
        drag = DragPage(webdriver_handler)
        drag.open_site()
        time.sleep(6)
        drag.drag_drop()










