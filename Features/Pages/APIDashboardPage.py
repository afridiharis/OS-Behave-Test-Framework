from CommonFuncs.WebCommon import find_element
from Features.Pages.BasePage import BasePage


class APIDashboard(BasePage):
    # Locators for the API Dashboard
    login_link = ('link', 'log in')
    signup_link = ('link', "sign up")
    doc_link = ('link', "documentation")


    def __init__(self, driver):
        super().__init__(driver)

    def get_login_link_text(self):
        return find_element(self.driver, *self.login_link).text

    def get_signup_link_text(self):
        return find_element(self.driver, *self.signup_link).text

    def get_doc_link_text(self):
        return find_element(self.driver, *self.doc_link).text