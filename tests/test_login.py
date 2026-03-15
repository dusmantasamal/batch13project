import time

import pytest

from Pages.login_page import LoginPage


class TestLogin:


    @pytest.mark.usefixtures('orange_hrm_potal')
    def test_verify_login_functionality(self):
        loginpage = LoginPage(self.driver)
        loginpage.enter_username("Admin")
        loginpage.enter_password("admin123")
        loginpage.click_on_login_btn()
        time.sleep(5)