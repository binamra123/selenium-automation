from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
   
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://practice.expandtesting.com/login")
gettext =driver.find_element(By.XPATH, value="//main[@class='flex-shrink-0 py-3']//p[1]").text
print(gettext)
time.sleep(3)