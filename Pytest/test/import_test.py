from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
   
@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    
def test_login(setup):
    driver.get("https://practice.expandtesting.com/login")
    driver.find_element(By.ID, value="username").send_keys("practice")
    driver.find_element(By.ID, value="password").send_keys("SuperSecretPassword!")  
    driver.find_element(By.XPATH, value="//button[@class='btn btn-bg btn-primary d-block w-100']").click()

def test_complete(setup):
    driver.close()
    print('Test Completed')
