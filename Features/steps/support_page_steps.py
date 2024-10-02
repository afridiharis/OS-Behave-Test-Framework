from behave import *
from Features.Pages.SupportPage import SupportPage


@step('side bar menu should show expanded faq links as below')
def check_side_bar_menu_links(context):
    context.support_page = SupportPage(context)
    side_bar_links = context.support_page.get_side_bar_links()
    expected_faq_links = context.table[0]['faqs_sub_links'].split(", ")
    for index, expected_link in enumerate(expected_faq_links):
        assert expected_link == side_bar_links[index].text, f"The side bar link is not as expected. "\
                                            " Expected: {}, Actual: {}".format(expected_link, side_bar_links[index].text)

@step('check all faqs are there')
def check_all_faqs(context):

    all_faqs = context.support_page.get_all_faqs()
    assert 10 == len(all_faqs), f"total number of faqs is not as expected. " \
                                " Expected: {}, Actual: {}".format(10, len(all_faqs))
    context.support_page.check_all_faqs()






