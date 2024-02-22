from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
   
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://practice.expandtesting.com/login")
getattr =driver.find_element(By.NAME, value="username").get_attribute('class')
print(getattr)
time.sleep(3)
driver.close()