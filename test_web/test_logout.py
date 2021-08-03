import delayed_assert
import pytest
import pytest_check
from pages.common_tasks import Common_Functions
from pages.yourwork_page import YourworkPage
from resource.read_xls import *
import allure
import logging as logger

# @pytest.mark.usefixtures("base_fixture")
class Test_logout(Common_Functions):
    @pytest.mark.webtest
    @allure.story("CBT-200 Logout from atlassian")
    @pytest.mark.parametrize("argvals", getcelldata("logoutTest", constants.DATASHEETPATH ))
    def test_logout(self, argvals):
        yourworkobject = self.do_login(argvals['Browser'].lower(), argvals['Username'], argvals['Password'])
        with allure.step("validating logout Page"):
            if pytest_check.is_instance(yourworkobject, YourworkPage):
                self.do_logout(yourworkobject)
                actualText = yourworkobject.get_text('logintoyouraccount_xpath')
                yourworkobject.validate_title(yourworkobject.prop['logout_title'])
                yourworkobject.validate_text(yourworkobject.prop['loginpagetext'], actualText)
                logger.info("Your work Page opened")
            else:
                logger.error("Your work page did not opened")
                logger.info("This is after all the assertions")
        delayed_assert.assert_expectations()
