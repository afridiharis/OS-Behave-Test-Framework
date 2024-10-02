from behave import *
from Features.Pages.HomePage import HomePage
from CommonFuncs.WebCommon import click, accept_cookies, is_element_displayed


@given('I am on the OS Data homepage')
def osdata_homepage(context):
    context.home_page = HomePage(context)
    context.execute_steps(u'''then page title should include "OS Data Hub"''')
    accept_cookies(context)


@when('I click on "{menu_button}" header menu button')
def click_header_menu_button(context, menu_button):
    for index, button in enumerate(context.home_page.get_header_menu_buttons()):
        if button.text == menu_button:
            click(button, context)
            break

@then('verify header menu is as expected as below')
def verify_header_menu_links(context):
    expected_header_menu_options = context.table[0]['header_menu_options'].split(", ")
    actual_menu_options = context.home_page.get_header_menu_links().text.split('\n')
    assert actual_menu_options == expected_header_menu_options, f"menu list is not as expected." \
        f"Expected: {expected_header_menu_options}, Actual: {actual_menu_options}"


@step('check "{sign_up}" and "{explore}" buttons are displayed')
def verify_buttons_are_displayed(context, sign_up, explore):
    assert context.home_page.sign_up_button_displayed(), f"{sign_up} button is not displayed"
    assert context.home_page.explore_button_displayed(), f"{explore} button is not displayed"


@step('check animation containers are displayed')
def verify_animation_containers(context):
    for i in range(1, 5):
        assert is_element_displayed(context, 'xpath', f"{context.home_page.locators['animation_container'][1]}[{i}]"), \
            f"Animation container number {i} is not displayed"
