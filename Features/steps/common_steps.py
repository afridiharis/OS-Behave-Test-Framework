import logging

from behave import *
from Features.Pages.BasePage import BasePage

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@then('page title should include "{expected_page_title}"')
def verify_page_title(context, expected_page_title):
    context.base_page = BasePage(context.driver)
    assert context.base_page.assert_page_title(expected_page_title), "The title is not as expected." \
            "Expected: {}, Actual: {}".format(expected_page_title, context.base_page.get_page_title())


@step('header text should say "{expected_page_header}"')
def verify_page_header_text(context, expected_page_header):
    context.base_page.assert_page_header_text(expected_page_header), "The title is not as expected. " \
            " Expected: {}, Actual: {}".format(expected_page_header, context.base_page.get_page_header_text())


@step('on the sidebar it should say "{expected_sidebar_text}"')
def verify_sidebar_header_text(context, expected_sidebar_text):
    assert context.base_page.assert_sidebar_header_text(expected_sidebar_text), "The sidebar is not as expected. " \
           "Expected: {}, Actual: {}".format(expected_sidebar_text, context.base_page.get_sidebar_header_text())


