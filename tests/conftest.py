import pytest

from Pages.base_action import BasePage
from utils.common_function import get_data_from_input_file

driver = None


@pytest.fixture(scope="function")
def orange_hrm_potal(request):
    global  driver
    browser = get_data_from_input_file("Browser")
    print("browser", browser)
    url = get_data_from_input_file("url")
    print("url", url)
    base_page = BasePage(driver= None)
    driver = base_page.open_browser(browser)
    base_page.launch_application(url)
    base_page.maximize_window()
    request.cls.driver = driver
    yield 
    base_page.tear_down()
