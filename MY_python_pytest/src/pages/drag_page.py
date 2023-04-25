from UI_test.UI_Test_3.MY_python_pytest.src.common.web_page_template import WebPageTemplate
from UI_test.UI_Test_3.MY_python_pytest.src.pages.base_page import BasePage
from UI_test.UI_Test_3.MY_python_pytest.src.locators.drag_page_locators import DragPageLocators
from selenium.webdriver.common.by import By


class DragPage(BasePage):

    def open_site(self):
        self.visit(url=DragPageLocators.url)

    def find_element(self, locator):
        selector = (By.XPATH, locator)
        self.web_driver_handler.find_element(*selector)

    def drag_drop(self):
        self.drag_and_drop(DragPageLocators.SOURCE_IMG, DragPageLocators.TRASH_FIELD)

    def refresh(self):
        self.refresh()







