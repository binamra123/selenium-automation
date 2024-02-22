from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class FindElementbyID():
    def locate_by_id(self):

       driver = driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
       driver.get("https://practicetestautomation.com//practice-test-login//")
       driver.find_element(By.ID, value= 'username').send_keys("student")
       driver.find_element(By.ID, value= 'password').send_keys("Password123")
       time.sleep(10)
findbyid = FindElementbyID()
findbyid.locate_by_id()
