from CommonFuncs.WebCommon import find_element, is_element_displayed
from Features.Pages.BasePage import BasePage


class HomePage(BasePage):
    # Locators for the Homepage
    locators = {
        "header_menu_links": ('xpath', "//div[@class='nav-actions-container']/nav"),
        "header_menu_buttons": ('css', "[role='tab']"),
        "sign_up_button": ('xpath', "//button[normalize-space()='Sign up for free']"),
        "explore_button": ('xpath', "//button[normalize-space()='Explore and access OpenData']"),
        "header_text": ('xpath', "//h1[text()='Welcome to the OS Data Hub']"),
        "animation_container": ('xpath', "//div[@data-testid='animation-container']")
    }

    def __init__(self, driver):
        super().__init__(driver)

    def get_header_menu_links(self):
        return find_element(self.driver, *self.locators['header_menu_links'])

    def get_header_menu_buttons(self):
        return find_element(self.driver, *self.locators['header_menu_buttons'], multiple=True)

    def get_sign_up_button(self):
        return find_element(self.driver, *self.locators['sign_up_button'])

    def get_explore_button(self):
        return find_element(self.driver, *self.locators['explore_button'])

    def get_header_text(self):
        return find_element(self.driver, *self.locators['header_text']).text

    def sign_up_button_displayed(self):
        return is_element_displayed(self.driver, element=self.get_sign_up_button())

    def explore_button_displayed(self):
        return is_element_displayed(self.driver, element=self.get_explore_button())

