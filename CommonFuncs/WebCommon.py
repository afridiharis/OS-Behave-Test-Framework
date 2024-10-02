import os
import pathlib
import time
import logging
from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def go_to(context, url):
    url = url.strip()
    context.driver.get(url)


# will check is an element is displayed or not via a boolean value or raise an exception
# if locator type isn't within supported types
def is_element_displayed(context, by=None, locator_value=None, element=None):

    try:
        if element is None:
            logging.info(f"Looking for element with {by} = '{locator_value}'")
            element = find_element(context, by, locator_value)

        if not element:
            logging.debug(f"Element not found with: {by} = '{locator_value}'")
            return False

        if element.is_displayed():
            logging.info(f"Element found and is displayed: {by} = '{locator_value}'")
            return True
        else:
            logging.debug(f"Element found but not visible: {by} = {locator_value}, trying to scroll into view.")

            # Scroll element into view using JavaScript
            context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(0.5)

            if element.is_displayed():
                logging.info(f"Element found and is displayed: {by} = {locator_value} after scrolling.")
                return True
            else:
                logging.error(f"Element located by {by} = {locator_value} is still not visible after scrolling.")
                if isinstance(context.driver, WebDriver):
                    take_screenshot(context, ss_name='element-not-visible')
                return False
    except Exception as e:
        logging.error(f"Unexpected Error in is_element_displayed: {e}")


def find_element(context, by, value, multiple=False):
    try:
        # list of all locator types:
        by_types = {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "class": By.CLASS_NAME,
            "tag": By.TAG_NAME,
            "link": By.LINK_TEXT,
            "partial_link": By.PARTIAL_LINK_TEXT
        }

        if by not in by_types:
            raise ValueError(f"Locator type '{by}' not supported")
        if multiple:
            logging.info(f"Attempting to find multiple elements by {by} with value '{value}'")
            elements = context.driver.find_elements(by_types[by], value)

            if elements:
                logging.info(f"Found {len(elements)} element(s) by {by} with value '{value}'")
                return elements
        else:
            logging.info(f"Attempting to find element by {by} with value '{value}'")
            element = context.driver.find_element(by_types[by], value)
            logging.info(f"Element found by {by} with value '{value}'")
            return element

    except NoSuchElementException as e:
        # Handle the specific NoSuchElementException
        logging.error(f"Element not found by {by} with value '{value}'")
        logging.error(f"Element not found: by {by} with value {value}. Taking screenshot")
        if isinstance(context.driver, WebDriver):
            take_screenshot(context)
        # Raise the exception to be handled if needed
        raise e

    except Exception as e:
        # Log other exceptions and propagate them
        logging.error(f"An unexpected error occurred: {e}")
        raise e
        # raise e  # Propagate any other exceptions


def accept_cookies(context):
    delay = 5  # seconds
    try:
        # wait for cookie buttons to load as there's a delay to when "Let me choose" button appears
        WebDriverWait(context.driver, delay).until(EC.visibility_of_element_located((By.XPATH, "//button[span[text()='Let me choose']]")))
        print("Page is ready!")

    except TimeoutException:
        logging.error("Loading took too much time!")

    accept = WebDriverWait(context.driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Accept']]")))
    click(accept, context)
    time.sleep(0.5)


def click(web_element, context):
    try:
        # wait for cookie buttons to load as there's a delay to when "Let me choose" button appears
       web_element.click()

    except ElementClickInterceptedException:
        element_name = web_element.text if web_element.text else ''
        logging.error(f"Couldn't click on given web element: {element_name} {web_element}")
        take_screenshot(context, ss_name=f'{element_name}_element_not_clicked')
        raise


def take_screenshot(context, ss_name='element_not_found'):
    scenario_name = context.scenario.name.replace(' ', '_')
    feature_name = context.feature.name.replace(' ', '_')
    curr_file_path = pathlib.Path(__file__).parent.parent.absolute()
    dir_to_create = os.path.join(curr_file_path, feature_name + '-feature-ss-' + time.strftime("%Y-%m-%d_%H-%M"))
    path = pathlib.Path(dir_to_create)
    if not path.exists():
        path.mkdir(exist_ok=True)
    # os.mkdir(dir_to_create)
    screenshot_path = dir_to_create
    ss_file_name = os.path.join(screenshot_path, f'{scenario_name}-{time.strftime("%M-%S")}-{ss_name}.png')
    context.driver.save_screenshot(ss_file_name)
    logging.debug(f"Screenshot {ss_name} failing saved at {ss_file_name}")



