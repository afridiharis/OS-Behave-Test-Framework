from behave import *
from CommonFuncs.WebCommon import is_element_displayed
from Features.Pages.DownloadPage import DownloadPage


@step('I can see the search bar')
def verify_search_bar(context):
    context.download_page = DownloadPage(context)
    search_bar = context.download_page.get_search_bar()
    assert is_element_displayed(context, element=search_bar)

@step('I can see the filters below the search bar as below')
def verify_search_filters(context):
    types_of_data_text = context.download_page.get_types_of_data_filter_text()
    types_of_providers_text = context.download_page.get_types_of_data_provider_text()
    expected_data_text = context.table[0]['filter_type']
    expected_provider_text = context.table[1]['filter_type']
    assert types_of_data_text == expected_data_text, f'expected type data: {expected_data_text} does not match actual: {types_of_data_text}'
    assert types_of_providers_text == expected_provider_text, f'expected providers data: {expected_data_text} does not match actual: {types_of_providers_text}'

@step('I can see all the download results displayed on the page')
def verify_all_download_results(context):
    total_results, total_downloads = context.download_page.get_total_results_and_total_downloads()
    assert total_results == total_downloads, f"number of total expected results: {total_results} isn't equal to actual downloads: {total_downloads}"

