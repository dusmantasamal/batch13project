from selenium.webdriver.common.by import By

from Pages.base_action import BasePage


class AdminPage(BasePage):


    Admin_link = (By.XPATH, '//span[text()="Admin"]')
    Admin_username = (By.XPATH,'//div[2]/input[@class="oxd-input oxd-input--active"]')
    Admin_Userrole = (By.XPATH,"//label[normalize-space()='User Role']/following::div[contains(@class,'oxd-select-text-input')][1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_admin_link(self):
        self.click_me(self.Admin_link)

    def select_username(self, value):
        self.type_word(self.Admin_username, value)
        
    def select_userrole(self):
        self.click_me(self.Admin_Userrole)