from pages.base import Base
from pages.yourwork_page import YourworkPage
from selenium import webdriver

class LoginPage(Base):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def login_page(self, username, password):
        print(f"Login Page Title - {self.driver.title}")
        self.type_data('username_xpath', username)
        self.click('continue_xpath')
        self.type_data('password_xpath', password)
        self.click('login_xpath')
        return YourworkPage(self.driver)