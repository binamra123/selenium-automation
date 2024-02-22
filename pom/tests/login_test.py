from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from pom.pages.login_page import LoginPage

@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield 
    driver.close()

    
def test_login(setup):
    login_page = LoginPage(driver)
    login_page.open_page("https://practice.expandtesting.com/login")
    login_page.enter_username("practice")
    login_page.enter_password("SuperSecretPassword!")
    time.sleep(2)
    login_page.click_login()


# def test_complete(setup):
#     driver.close()
#     print('Test Completed')
