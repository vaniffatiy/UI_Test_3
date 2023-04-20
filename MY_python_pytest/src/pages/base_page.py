#
# from MY_python_pytest.src.common.web_page_template import WebPageTemplate
# from MY_python_pytest.src.config import Config
# from MY_python_pytest.src.locators.main_page_locators import MainPageLocators
# from MY_python_pytest.src.pages.downloads_page import DownloadsPage
#
#
# class BasePage(WebPageTemplate):
#
#     def visit(self, url, locator):
#         self.visit_and_verify(url, locator)
#
#
#     def switch_to(self,locator):
#         self.verify_page_has_been_loaded(locator)
#
#
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from seleniumpagefactory.Pagefactory import PageFactory
#
#
# class BasePage(PageFactory):
#
#     def do_click(self, by_locator):
#         return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click
#
#     def do_send_keys(self, by_locator, text):
#         return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
#
#     def check_if_visible(self, by_locator):
#         button_check = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
#         return bool(button_check)
