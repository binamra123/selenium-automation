from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
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


def  test_copy(setup):
    login_page = LoginPage(driver)
    login_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    login_page.enter_username("admin.dhangadhi")
    login_page.enter_password("password")
    time.sleep(2)
    login_page.click_login()
    time.sleep(3)
    assert driver.title == "Projects | Infrastructure Management System Stage"
