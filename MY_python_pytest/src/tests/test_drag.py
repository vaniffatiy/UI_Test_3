from UI_test.UI_Test_3.MY_python_pytest.src.pages.drag_page import DragPage
import time


class TestDynamic:

    def test_drag_drop(self, webdriver_handler):
        drag = DragPage(webdriver_handler)
        drag.open_site()
        drag.drag_drop()
        drag.drag_drop_offset()










