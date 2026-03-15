from selenium import webdriver


class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def open_browser(self, browser_name):
        print("browser name ", browser_name)
        if browser_name == "chrome":
           self.driver = self.open_chrome()
           return self.driver
        elif browser_name == "firefox":
            self.driver = self.open_firefox()
            return self.driver
        else:
            self.driver = self.open_edge()
            return self.driver

    def open_chrome(self):
        return webdriver.Chrome()

    def open_edge(self):
        return webdriver.Edge()

    def open_firefox(self):
        return webdriver.Firefox()

    def launch_application(self, url):
        self.driver.get(url)

    def maximize_window(self):
        self.driver.maximize_window()

    def tear_down(self):
        self.driver.quit()

    def get_web_element(self, locator):
        element = self.driver.find_element(locator[0], locator[1])
        return element

    def get_web_elements(self, locator):
        element = self.driver.find_elements(locator[0], locator[1])
        return element

    def click_me(self, locator):
        try:
            element = self.get_web_element(locator)
            element.click()
        except Exception as e:
            print("exception occrus as ", e)


    def type_word(self, locator, value):
        try:
            element = self.get_web_element(locator)
            element.send_keys(value)
        except Exception as e:
            print("exception occrus as ", e)



