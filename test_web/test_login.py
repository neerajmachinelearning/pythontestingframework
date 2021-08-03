import delayed_assert
import pytest
import pytest_check
from pages.common_tasks import Common_Functions
from pages.yourwork_page import YourworkPage
from resource.read_xls import *
import allure
import logging as logger

class Test_Login(Common_Functions):
    @pytest.mark.webtest
    @allure.story("CBT-199 Login to atlassian")
    @pytest.mark.parametrize("argvals", getcelldata("loginTest", constants.DATASHEETPATH ))
    def test_login(self, argvals):
        yourworkobject = self.do_login(argvals['Browser'].lower(), argvals['Username'], argvals['Password'])
        with allure.step("Validating login page"):
            if pytest_check.is_instance(yourworkobject, YourworkPage):
                expectedTitle = yourworkobject.prop['yourworkpage_title']
                # yourworkobject.yourwork_page()
                yourworkobject.validate_title(expectedTitle)
                logger.info("Your work page opened")
            else:
                logger.error("Your work page did not opened")
        logger.info("This is after all the assertions")
        delayed_assert.assert_expectations()

    @pytest.mark.webtest
    @allure.story("CBT-199 Login to atlassian")
    def test_2(self):
        with allure.step("Validating test_2"):
            logger.info("Inside test_3")

    @pytest.mark.webtest
    @allure.story("CBT-199 Login to atlassian")
    def test_3(self):
        with allure.step("validating test_3"):
            # pytest.fail("test_3 failed")
            logger.info("inside test_3")

    #
    #
    #     with allure.step("Validating email"):
    #         logger.info("Inside test_email")
    #         assert True

