from behave import *
from CommonFuncs.WebCommon import is_element_displayed
from Features.Pages.PlansPage import PlansPage


@step('sub heading should say "{expected_pick_plan}"')
def verify_sub_heading(context, expected_pick_plan):
    context.plans_page = PlansPage(context)
    actual_sub_heading = context.plans_page.get_plan_header().text
    assert expected_pick_plan == actual_sub_heading, f"The sub heading is not as expected. "\
                                " Expected: {}, Actual: {}".format(expected_pick_plan, actual_sub_heading)


@step('all three plans should be shown as below')
def verify_all_plans(context):
    actual_plans = context.plans_page.get_all_plans()
    expected_plans = context.table[0]['plans'].split(", ")
    for index, expected_plan in enumerate(expected_plans):
        assert is_element_displayed(context, element=actual_plans[index])
        assert expected_plan == actual_plans[index].text, f"The plan is not as expected. "\
                                " Expected: {}, Actual: {}".format(expected_plan, actual_plans[index].text)








