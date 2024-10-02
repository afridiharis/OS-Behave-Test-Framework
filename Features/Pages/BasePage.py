import time

from CommonFuncs.WebCommon import find_element


class BasePage:
    # locators
    page_header_title = ('tag', "h1")
    sidebar_header_text = ('xpath', "//li[starts-with(@id, 'Menu.')][1]")


    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def get_sidebar_header_text(self):
        return find_element(self, *self.sidebar_header_text).text

    def get_page_header_text(self):
        return find_element(self, *self.page_header_title).text

    def assert_page_title(self, expected_title):
        actual_title = self.get_page_title()
        time.sleep(0.5)
        return expected_title in actual_title

    def assert_page_header_text(self, expected_page_header):
        return expected_page_header == self.get_page_header_text

    def assert_sidebar_header_text(self, expected_sidebar_text):
        return expected_sidebar_text == self.get_sidebar_header_text()

