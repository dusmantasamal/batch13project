import time

from selenium.webdriver.common.by import By

from Pages.base_action import BasePage


class LoginPage(BasePage):

    USERNAME= (By.XPATH, "//input[@name='username']")
    PASSWORD= (By.XPATH, "//input[@name='password']")
    LOGIN_BTN= (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_username(self, value):
        time.sleep(10)
        self.type_word(self.USERNAME, value)

    def enter_password(self, value):
        self.type_word(self.PASSWORD, value)

    def click_on_login_btn(self):
        self.click_me(self.LOGIN_BTN)