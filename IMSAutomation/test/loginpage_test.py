from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
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

    
def test_login(setup):
    login_page = LoginPage(driver)
    login_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    login_page.enter_username("admin.dhangadhi")
    login_page.enter_password("password")
    time.sleep(2)
    login_page.click_login()
    time.sleep(3)
    assert driver.title == "Projects | Infrastructure Management System Stage"


def test_invalogin(setup):
    login_page = LoginPage(driver)
    login_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    login_page.enter_username("admin")
    login_page.enter_password("abcd")
    time.sleep(2)
    login_page.click_login()
    time.sleep(3)
    


def  test_invaname(setup):
    login_page = LoginPage(driver)
    login_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    login_page.enter_username("admin")
    login_page.enter_password("password")
    time.sleep(2)
    login_page.click_login()
    time.sleep(3)


def  test_invapass(setup):
    login_page = LoginPage(driver)
    login_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    login_page.enter_username("admin.dhangadhi")
    login_page.enter_password("admin")
    time.sleep(2)
    login_page.click_login()
    time.sleep(3)

def  test_blankcred(setup):
    login_page = LoginPage(driver)
    login_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    login_page.enter_username("")
    login_page.enter_password("")
    time.sleep(2)
    login_page.click_login()
    time.sleep(3)

def  test_remember(setup):
    login_page = LoginPage(driver)
    login_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    login_page.enter_username("admin.dhangadhi")
    login_page.enter_password("password")
    time.sleep(2)
    checkbox = driver.find_element(By.CLASS_NAME, value='checkmark')
    ActionChains(driver).move_to_element(checkbox).click().perform()
    login_page.click_login()
    time.sleep(3)

def  test_space(setup):
    login_page = LoginPage(driver)
    login_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    login_page.enter_username(" ")
    login_page.enter_password(" ")
    time.sleep(2)
    login_page.click_login()
    time.sleep(3)

def  test_copy(setup):
    login_page = LoginPage(driver)
    login_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    login_page.enter_username("admin.dhangadhi")
    login_page.enter_password("password")
    time.sleep(2)
    copying = driver.find_element(By.ID, value='password')
    ActionChains(driver).context_click(copying).perform()
    time.sleep(3)