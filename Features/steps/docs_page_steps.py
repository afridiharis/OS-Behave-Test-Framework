from behave import *
from Features.Pages.DocsPage import DocsPage


@step('verify all the links on the sidebar when expanding using details below')
def verify_sidebar_and_all_its_expanded_links(context):
    expected_sub_links = context.table[0]['side_menu_links'].split(", ")
    context.download_page = DocsPage(context)
    context.download_page.check_all_expanded_side_bar_links(expected_sub_links)



