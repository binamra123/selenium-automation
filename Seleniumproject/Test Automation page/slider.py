from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
   
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://practice.expandtesting.com/horizontal-slider")
a = driver.find_element(By.XPATH, value="//input[@value='0']")
action_chains = ActionChains(driver)
action_chains.drag_and_drop_by_offset(a,1.5,0).perform()
time.sleep(2)