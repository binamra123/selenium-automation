from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from pom.pages.signup_page import SignupPage
   
@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield 
    driver.close()

    
def test_signup(setup):
    signup_page = SignupPage(driver)
    signup_page.open_page("https://practice.expandtesting.com/inputs")
    signup_page.enter_number("1234")
    signup_page.enter_text("tests")
    signup_page.enter_password("tests123")
    signup_page.enter_date("03/05/2023")
    time.sleep(2)
    signup_page.click_display()
    time.sleep(2)
    signup_page.click_clear()



# def test_complete(setup):
#     driver.close()
#     print('Test Completed')
