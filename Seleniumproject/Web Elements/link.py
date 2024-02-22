from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
   
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://practicetestautomation.com/practice-test-login/")

#driver.find_element(By.LINK_TEXT, value="COURSES").click()
driver.find_element(By.XPATH, value="//*[@id='menu-item-21]/a").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, value="PRACTI").click()
time.sleep(10)