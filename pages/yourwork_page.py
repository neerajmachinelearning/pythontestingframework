from pages.base import Base


class YourworkPage(Base):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def yourwork_page(self):
        self.logger.info(f"yourwork Page Title - {self.driver.title}")
        print("after failure")

    def yourwork_logout(self):
        self.logger.info("Logging out from yourwork page")
        self.click('user_xpath')
        self.click('logout_xpath')
        self.click('logoutbutton_xpath')


    # def yourwork_validatetext(self):
    #     actualText = self.driver.find_element_by_xpath(self.prop["viewallProject_xpath"]).text
    #     if actualText == "View all projects":
    #         assert True
    #     else:
    #         assert False




