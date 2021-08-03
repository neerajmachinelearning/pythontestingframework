import base64
import logging
import time
from datetime import datetime

from allure_commons.types import AttachmentType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_web import conftest
import logging as logger
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
import allure

from resource import constants
import delayed_assert


class Base():

    def __init__(self):
        self.driver = None
        self.prop = conftest.prop
        self.logger = logger.getLogger()
        self.logger.setLevel(logging.INFO)
        # self.env = conftest.env

## Selenium Web functions
    def open_browser(self, browser):
        with allure.step(f"Opening Browser {browser}"):
            if self.prop['GridRun'].lower() == constants.GRIDRUN_Y.lower():
                self.logger.info("Running in Grid")
                if browser == 'chrome':
                    caps = DesiredCapabilities.CHROME.copy()
                    caps['browserName'] = 'chrome'
                    caps['javascriptEnabled'] = True
                    caps['platform'] = 'ANY'
                elif browser == 'firefox':
                    caps = DesiredCapabilities.FIREFOX.copy()
                    caps['browserName'] = 'firefox'
                    caps['javascriptEnabled'] = True
                    caps['platform'] = 'ANY'
                elif browser == 'edge':
                    caps = DesiredCapabilities.CHROME.copy()
                    caps['browserName'] = 'MicrosoftEdge'
                    caps['javascriptEnabled'] = True
                    caps['platform'] = 'ANY'
                try:
                    self.driver = webdriver.Remote(command_executor='http://localhost:4446/wd/hub', desired_capabilities=caps)
                except Exception as e:
                    print(e)
                return self.driver
            else:
                self.logger.info("Running from local")
                if browser == 'chrome':
                    options = webdriver.ChromeOptions()
                    options.add_argument("--disable-infobars")
                    options.add_argument("-disable-notifications")
                    options.add_argument("--start-maximized")
                    self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
                elif browser == 'firefox':
                    self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
                elif browser == 'edge':
                    self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
                    self.driver.maximize_window()
                else:
                    self.driver = webdriver.Ie()
                    self.driver.maximize_window()
                return self.driver

    def quit_driver(self):
        with allure.step(f"Quiting Browser"):
            if self.driver != None:
                self.driver.quit()

    def take_screen_shots(self):
        allure.attach(self.driver.get_screenshot_as_png(), "Screen shot taken at: "+str(datetime.now()), AttachmentType.PNG)

    def navigate(self, url):
        with allure.step(f"Navigating to {url}"):
            self.driver.get(url)
            self.take_screen_shots()

    def click(self, locator):
        with allure.step(f"Clicking on; {locator}"):
            self.getelement(locator).click()
            self.take_screen_shots()

    def type_data(self, locator, data):
        with allure.step(f"Enter data on locator: {locator}"):
            self.getelement(locator).send_keys(data)

    def get_text(self, locator):
        with allure.step(f"Get text present on locator: {locator}"):
            actualtext = self.getelement(locator).text
        return actualtext


    def waitforpagetobeloaded(self):
        i = 0
        while i != 10:
            load_status = self.driver.execute_script("return document.readyState")
            if load_status == 'complete':
                break
            else:
                time.sleep(2)
                i = i+1

    def is_element_present(self, locator):
        wait = WebDriverWait(self.driver, 20)
        element = self.prop[locator]
        self.waitforpagetobeloaded()
        if locator.endswith('_xpath'):
            elementList = wait.until(EC.presence_of_all_elements_located((By.XPATH, element)))
        elif locator.endswith('_id'):
            elementList = wait.until(EC.presence_of_elements_located((By.ID, element)))
        elif locator.endswith('_name'):
            elementList = wait.until(EC.presence_of_elements_located((By.NAME, element)))
        elif locator.endswith('_cssSelector'):
            elementList = wait.until(EC.presence_of_elements_located((By.CSS_SELECTOR, element)))
        else:
            elementList = wait.until(EC.presence_of_elements_located((By.TAG_NAME, element)))

        if len(elementList)==0:
            return False
        else:
            return True

    def is_element_visible(self, locator):
        wait = WebDriverWait(self.driver, 20)
        element = self.prop[locator]
        self.waitforpagetobeloaded()
        if locator.endswith('_xpath'):
            elementList = wait.until(EC.visibility_of_all_elements_located((By.XPATH, element)))
        elif locator.endswith('_id'):
            elementList = wait.until(EC.visibility_of_all_elements_located((By.ID, element)))
        elif locator.endswith('_name'):
            elementList = wait.until(EC.visibility_of_all_elements_located((By.NAME, element)))
        elif locator.endswith('_cssSelector'):
            elementList = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, element)))
        else:
            elementList = wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, element)))

        if len(elementList) == 0:
            return False
        else:
            return True

    def getelement(self, locator):
        obj = self.prop[locator]
        if self.is_element_present(locator) and self.is_element_visible(locator):
            try:
                if locator.endswith('_xpath'):
                    element = self.driver.find_element_by_xpath(obj)
                elif locator.endswith('_id'):
                    element = self.driver.find_element_by_id(obj)
                elif locator.endswith('_name'):
                    element = self.driver.find_element_by_name(obj)
                elif locator.endswith('_cssSelector'):
                    element = self.driver.find_element_by_css_selector(obj)
                else:
                    return False
                return element
            except Exception:
                logger.error("Element Not Found")
        else:
            logger.error("Element either not present or not visible")

# utility functions
    def encrypt_message(self, message):
        encoded_data = base64.b64encode(message).decode(encoding="utf-8")
        return encoded_data

    def decrypt_message(self, encMessage):
        decoded_data = base64.b64decode(encMessage).decode(encoding="utf-8")
        return decoded_data

    def report_success(self, message):
        assert True

    def report_failure(self, message):
        self.take_screen_shots()
        assert False

##  validate Functions
    def validate_title(self, expectedTitle):
        actualTitle = self.driver.title
        with allure.step(f"Validating expected title {expectedTitle}"):
            delayed_assert.expect(expectedTitle == actualTitle, f"Expected Title: {expectedTitle}, Actual Title:{actualTitle}")
            # if delayed_assert.expect(expectedTitle, actualTitle):
            #     self.logger.info(f"Expected Title: {expectedTitle}, Actual Title:{actualTitle}")
            #     print(f"Expected Title: {expectedTitle}, Actual Title:{actualTitle}")
            #     # self.report_success(f"Expected Title: {expectedTitle}, Actual Title:{actualTitle}")
            #     delayed_assert.assert_expectations()
            # else:
            #     self.logger.error(f"Expected Title: {expectedTitle}, Actual Title:{actualTitle}")
            #     allure_pytest.utils.allure_labels()

            # try:
            #     assert expectedTitle == actualTitle
            # except AssertionError as e:
            #     pytest.fail(f"expectedTitle: {expectedTitle} and actualTitle: {actualTitle} not matching")
            # b = check.equal(expectedTitle, actualTitle)

    def validate_text(self, expectedText, actualText):
        with allure.step(f"Validating text {expectedText} vs {actualText}"):
            delayed_assert.expect(expectedText == actualText, f"expectedText: {expectedText} and actualText: {actualText} not matching")
            # try:
            #     assert expectedText, actualText
            # except AssertionError as e:
            #     pytest.fail(f"expectedText: {expectedText} and actualText: {actualText} not matching")





