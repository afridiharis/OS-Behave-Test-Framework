from behave import *
from Features.Pages.APIDashboardPage import APIDashboard


@step('text links should say "{log_in}", "{sign_up}" and "{doc}" on main content of the page')
def verify_page_links(context, log_in, sign_up, doc):
    context.api_page = APIDashboard(context)
    login_link_text = context.api_page.get_login_link_text()
    signup_link_text = context.api_page.get_signup_link_text()
    doc_link_text = context.api_page.get_doc_link_text()
    assert log_in == login_link_text, f"Expected: {log_in} is not same as Actual: {login_link_text}"
    assert sign_up == signup_link_text, f"Expected: {sign_up} is not same as Actual: {signup_link_text}"
    assert doc == doc_link_text, f"Expected: {doc} is not same as Actual: {doc_link_text}"


