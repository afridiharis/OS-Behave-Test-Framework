import logging

from CommonFuncs.WebCommon import find_element, is_element_displayed
from Features.Pages.BasePage import BasePage


class DocsPage(BasePage):

    # expand_all = custom_find_element(context, 'xpath', "//span[text()='Expand All']")
    # expected_links = custom_find_element(context, 'xpath', "//span[text()='Close all']/parent::div/following-sibling::ul/li")
    # list_items = sidebar.find_elements('xpath', "./li")
    # //li[contains(@id,'Menu.')]
    # if section.text == 'Legal':
    #     expected_legal_links = custom_find_element(context, 'xpath', "//main//ul[position()>1]/li", multiple=True)
    # Locators for the Docs Page
    locators = {
        "nav_bar": ('xpath', "//ul[@aria-label='Secondary']/li"),
        "page_header_title": ('tag', "h1")
    }

    def __init__(self, driver):
        super().__init__(driver)

    def get_side_bar_nav(self):
        return find_element(self.driver, *self.locators['nav_bar'], multiple=True)

    def check_all_expanded_side_bar_links(self, expected_sub_links):

        for index, section in enumerate(self.get_side_bar_nav(), start=1):
            if section.text == 'Docs':
                continue
            section.click()
            logging.info(f"Section text is: {section.text}")
            nav_bar = self.locators['nav_bar'][1]

            sub_links = find_element(self.driver,'xpath', f"{nav_bar}[{index}]/following-sibling::li/ul/li",
                                                                                   multiple=True)
            if not sub_links:
                raise AssertionError(f"Expected links shown when expanding the section but got: {sub_links} for section: {section.text}")

            for sub_index, expected_sub_link in enumerate(expected_sub_links):
                current_actual_link = sub_links[sub_index]
                current_actual_link.click()
                expected_page_title = current_actual_link.text if section.text in ['Legal', 'Our brand logo'] else f"{section.text}: {expected_sub_link}"
                actual_page_title = find_element(self.driver, *self.locators['page_header_title'])
                assert is_element_displayed(self.driver, element=actual_page_title)
                assert expected_page_title in actual_page_title.text, (f"Expected page title: {expected_page_title}"
                                                                       f" don't match actual title: {actual_page_title.text}")
                assert is_element_displayed(self.driver, element=current_actual_link)
                if section.text not in ['Legal', 'Our brand logo']:
                    assert expected_sub_link == current_actual_link.text, f'expected: {expected_sub_link} and actual: {current_actual_link} dont match'

                logging.info(f"Now checking at section: {section.text} and sub_links:: {sub_links[sub_index].text}")
