from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
   
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://practice.expandtesting.com/#examples")
driver.find_element(By.XPATH, value="//*[contains(text(),'Web inputs')]").click()
time.sleep(1)
driver.find_element(By.XPATH, value="//input[@id='input-number']").send_keys('1234')
time.sleep(1)
driver.find_element(By.XPATH, value="//input[@id='input-text']").send_keys('abcd')
time.sleep(1)
driver.find_element(By.XPATH, value="//input[@id='input-password']").send_keys('password')
time.sleep(1)
driver.find_element(By.XPATH, value="//input[@id='input-date']").send_keys('02/01/2023')
time.sleep(1)
driver.find_element(By.XPATH, value="//button[@id='btn-display-inputs']").click()
time.sleep(3)
driver.find_element(By.XPATH, value="//button[@id='btn-clear-inputs']").click()

time.sleep(3)

