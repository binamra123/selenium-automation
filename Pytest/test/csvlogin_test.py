import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def readData():
    data_list = []
    csv_file = "C:\\Users\\Admin\\OneDrive\\Desktop\\testlogin.csv" 

    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            data_list.append((row[0], row[1]))  
    return data_list

@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password", readData())
def test_login(setup, username, password):
    driver = setup
    driver.get("https://practice.expandtesting.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)  
    driver.find_element(By.XPATH, "//button[@class='btn btn-bg btn-primary d-block w-100']").click()
    time.sleep(3)

def test_complete():
    print('Test Completed')
