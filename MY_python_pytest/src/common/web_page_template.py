class WebPageTemplate:

    def __init__(self, webdriver_handler):
        self.web_driver_handler = webdriver_handler
        self.web_elements_cache = {}

    def get_element(self, selector):
        element = self.web_driver_handler.find_element(selector)
        return element

    def verify_page_has_been_loaded(self, selector):
        """
        find the most obvious element that is always present on a page that you just opened
        and if it's found then good, otherwise assume page could not be loaded and throw an exception
        :return:
        """
        self.web_driver_handler.find_element(selector)

    def visit(self, url):
        # go to the main page
        self.web_driver_handler.visit(url)
        # verify it was loaded
        # self.verify_page_has_been_loaded(verification_selector)

    def select_tab(self, index):
        """
        sometimes need to switch tabs if for example url redirect causes to open a new tab
        :param index:
        :return:
        """
        self.web_driver_handler.select_tab(index)
