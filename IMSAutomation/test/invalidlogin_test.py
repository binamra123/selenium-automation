from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
import warnings
from IMSAutomation.pages.loginpage import LoginPage

@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield 
    driver.close()

    
def test_invalogin(setup):
    login_page = LoginPage(driver)
    login_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    login_page.enter_username("admin")
    login_page.enter_password("abcd")
    time.sleep(2)
    login_page.click_login()
    time.sleep(3)

    # message = login_page.get_error_message()      
    # assert message == 'These credentials do not match our records.'
    
    with pytest.raises(ValueError) as e:
        raise ValueError("These credentials do not match our records.")
    
    assert str(e.value) == 'These credentials do not match our records.'

    # with pytest.warns(UserWarning) as warning_info:
    #     login_page.click_login()
    
    # assert len(warning_info) == 1
    # assert str(warning_info[0].message) == "These credentials do not match our records."





# def  test_copy(setup):
#     login_page = LoginPage(driver)
#     login_page.open_page("https://admin.ims.staging.yipl.com.np/login")
#     login_page.enter_username("admin.dhangadhi")
#     login_page.enter_password("password")
#     time.sleep(2)
#     login_page.click_login()
#     time.sleep(3)
#     assert driver.title == "Projects | Infrastructure Management System Stage"
