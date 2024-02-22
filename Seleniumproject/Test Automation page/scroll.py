from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
   
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://practice.expandtesting.com/#examples")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.find_element(By.XPATH, value="//*[contains(text(),'Expand Testing')]").click()
time.sleep(3)
driver.close()