import logging
import time

from selenium import webdriver
from CommonFuncs import ConfigReader


def before_all(context):

    # Sets up the reporting html tool to embed screenshots

    for formatter in context._runner.formatters:
        if formatter.name == "html-pretty":
            context.formatter = formatter

def before_scenario(context,driver):
    browser = ConfigReader.read_test_config('test config', 'browser')
    print(f"this is browser: {browser}")
    if browser.lower() == 'firefox':
        context.driver = webdriver.Firefox()
    elif browser.lower() == 'chrome':
        context.driver = webdriver.Chrome()
    else:
        raise Exception("The browser '{}' is not supported".format(browser))
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_test_config('test config', 'url'))

def after_scenario(context, driver):
    context.driver.quit()

# Using the html reporting tool attaches the screenshot to the html behave report
def after_step(context, step):
    if step.status == 'failed':
        context.embed = context.formatter.embed
        file_path = f'reports/failed_screenshot.png_{time.strftime("%Y-%m-%d_%H-%M-%S")}.png'
        context.driver.get_screenshot_as_file(file_path)
        context.embed(mime_type="image/png", data=file_path, caption="Failed Screenshot")
