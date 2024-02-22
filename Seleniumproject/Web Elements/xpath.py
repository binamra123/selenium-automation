from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
   
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://practicetestautomation.com//practice-test-login//")
driver.find_element(By.XPATH, value="//input[@id='username']").send_keys('student')
driver.find_element(By.XPATH, value="//input[@id='password']").send_keys('Password123')
driver.find_element(By.XPATH, value="//button[@id='submit']").click()

time.sleep(10)
