from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from CommonFuncs.WebCommon import find_element
from Features.Pages.BasePage import BasePage


class DownloadPage(BasePage):
    # Locators for the Downloads Page
    locators = {
        "search_bar": ('id', 'search'),
        "types_of_data_filter": ('id', 'dataFilter'),
        "types_of_provider_filter": ('id', 'providerFilter'),
        "total_results_text": ('xpath', "//p[contains(text(), 'Results')]"),
        "total_downloads": ('xpath', "//div[@data-testid='downloads']//span[text()='Free OpenData']")
    }

    def __init__(self, driver):
        super().__init__(driver)

    def get_search_bar(self):
        return find_element(self.driver, *self.locators['search_bar'])

    def get_types_of_data_filter_text(self):
        return find_element(self.driver, *self.locators['types_of_data_filter']).text

    def get_types_of_data_provider_text(self):
        return find_element(self.driver, *self.locators['types_of_provider_filter']).text

    def get_results_to_be_loaded(self):
        WebDriverWait(self.driver.driver, 10).until(EC.text_to_be_present_in_element(self.locators['total_results_text'], "Results"))


    def get_total_results_and_total_downloads(self):
        self.get_results_to_be_loaded()
        total_results = find_element(self.driver, *self.locators['total_results_text']).text
        total_results = int(total_results.split()[0])
        total_downloads = find_element(self.driver, *self.locators['total_downloads'], multiple=True)
        return total_results, len(total_downloads)
