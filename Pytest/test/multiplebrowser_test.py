import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser") 

    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()))
    elif browser == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError("Invalid browser specified")

    yield driver 
    driver.quit()  

def pytest_addoption(parser):
    parser.addoption("--browser")

def test_login(setup):
    driver = setup
    driver.get("https://practicetestautomation.com//practice-test-login//") 
    driver.find_element(By.ID, 'username').send_keys("student")
    driver.find_element(By.ID, 'password').send_keys("Password123")
    time.sleep(3)  


