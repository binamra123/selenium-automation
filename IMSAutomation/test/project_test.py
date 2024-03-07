from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from IMSAutomation.pages.project import ProjectPage

@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield 
    driver.close()

    
def test_exstname(setup):
    project_page = ProjectPage(driver)
    project_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    project_page.enter_username("admin.dhangadhi")
    project_page.enter_password("password")
    time.sleep(2)
    project_page.click_login()
    time.sleep(2)
    project_page.search_field("test")
    time.sleep(2)


def test_nonexstname(setup):
    project_page = ProjectPage(driver)
    project_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    project_page.enter_username("admin.dhangadhi")
    project_page.enter_password("password")
    time.sleep(2)
    project_page.click_login()
    time.sleep(2)
    project_page.search_field("abcd")
    time.sleep(2)


def test_engtonep(setup):
    project_page = ProjectPage(driver)
    project_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    project_page.enter_username("admin.dhangadhi")
    project_page.enter_password("password")
    time.sleep(2)
    project_page.click_login()
    time.sleep(2)
    project_page.english_con()
    time.sleep(3)
    project_page.search_field("abcd")
    time.sleep(3)
    project_page.nepali_con()
    time.sleep(3)


def test_filter(setup):
    project_page = ProjectPage(driver)
    project_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    project_page.enter_username("admin.dhangadhi")
    project_page.enter_password("password")
    time.sleep(3)
    project_page.click_login()
    time.sleep(2)
    project_page.filter_button()
    time.sleep(2)
    project_page.radio_opt2()
    time.sleep(2)


def test_addproject(setup):
    project_page = ProjectPage(driver)
    project_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    project_page.enter_username("admin.dhangadhi")
    project_page.enter_password("password")
    time.sleep(3)
    project_page.click_login()
    time.sleep(3)
    project_page.add_project()
    time.sleep(2)
    
def test_importproject(setup):
    project_page = ProjectPage(driver)
    project_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    project_page.enter_username("admin.dhangadhi")
    project_page.enter_password("password")
    time.sleep(3)
    project_page.click_login()
    time.sleep(3)
    project_page.import_project()
    time.sleep(2)

def test_socialproject(setup):
    project_page = ProjectPage(driver)
    project_page.open_page("https://admin.ims.staging.yipl.com.np/login")
    project_page.enter_username("admin.dhangadhi")
    project_page.enter_password("password")
    time.sleep(3)
    project_page.click_login()
    time.sleep(3)
    project_page.project_social()
    time.sleep(2)




