class ParidaPage:
    USERNAME = (By.XPATH, "//input[@name='username']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
pass