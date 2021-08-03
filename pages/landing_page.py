from pages.base import Base
from pages.login_page import LoginPage

class LandingPage(Base):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def landing(self):
        self.navigate(self.prop["url"])
        print(f"Landing Page Title - {self.driver.title}")
        return LoginPage(self.driver)





