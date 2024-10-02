import logging

from CommonFuncs.WebCommon import find_element, go_to
from Features.Pages.BasePage import BasePage


class SupportPage(BasePage):
    # Locators for the Support Page
    locators = {
        "side_bar_links": ('xpath', "//ul[@aria-label='Secondary']/li[2]//li"),
        "all_faqs": ('xpath', "//nav[contains(@class, 'faqs-')]/ul/li//a"),
        "faq_titles": ('xpath', "//h3[@data-testid='faq-title']")
    }

    def __init__(self, driver):
        super().__init__(driver)

    def get_side_bar_links(self):
        return find_element(self.driver, *self.locators['side_bar_links'], multiple=True)

    def get_all_faqs(self):
        return find_element(self.driver, *self.locators['all_faqs'], multiple=True)

    def check_all_faqs(self):
        for index, faq in enumerate(self.get_all_faqs()):
            logging.info(f"faq attribute href is: {faq.get_attribute('href')}")
            expected_faq_header = faq.text
            go_to(self.driver, faq.get_attribute('href'))
            faq_title_locator = f"{self.locators['faq_titles'][1]}[{index + 1}]"
            actual_faq_header = find_element(self.driver, 'xpath', faq_title_locator).text
            assert expected_faq_header == actual_faq_header, f"The faq header title is not as expected. " \
                                 " Expected: {}, Actual: {}".format(expected_faq_header, actual_faq_header)
