# Actions funtions
import allure
import pytest

from test_web.conftest import obj_list
from pages.landing_page import LandingPage

@pytest.mark.usefixtures("base_fixture")
class Common_Functions():
    def do_login(self, browsername, username, password):
        with allure.step("Performing login to the Application"):
            for i in range(0, len(obj_list)):
                pass
            self.driver = obj_list[i].open_browser(browsername)
                # self.driver = self.open_browser(browsername)
            self.password = obj_list[i].decrypt_message(password)
            landing = LandingPage(self.driver)
            login_obj = landing.landing()
            yourworkobject = login_obj.login_page(username, self.password)
            return yourworkobject

    def do_logout(self, yourworkobject):
        with allure.step("Performing Logout function"):
            yourworkobject.yourwork_page()
            yourworkobject.yourwork_logout()