from UI_test.UI_Test_3.MY_python_pytest.src.config import Config
from UI_test.UI_Test_3.MY_python_pytest.src.common.web_page_template import WebPageTemplate
from UI_test.UI_Test_3.MY_python_pytest.src.locators.dynamic_home_locators import DynamicHomeLocators


class DynamicHome(WebPageTemplate):

    def open_site(self):
        self.visit_and_verify(url=Config.app_host+DynamicHomeLocators.url, verification_selector=DynamicHomeLocators.dynamic_btn)

    def find_element(self):
        self.get_element(selector=DynamicHomeLocators.dynamic_btn)

    def refresh(self):
        self.refresh()







