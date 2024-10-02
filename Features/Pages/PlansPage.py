from CommonFuncs.WebCommon import find_element
from Features.Pages.BasePage import BasePage


class PlansPage(BasePage):
    page_sub_header = ('xpath', "//h2[text()='Choose Your Plan']")
    plans = ('xpath', '//article/h3')


    def __init__(self, driver):
        super().__init__(driver)


    def get_plan_header(self):
        return find_element(self.driver, *self.page_sub_header)

    def get_all_plans(self):
        return find_element(self.driver, *self.plans, multiple=True)