from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
   
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://practice.expandtesting.com/drag-and-drop")

elem1 =driver.find_element(By.XPATH, value="//*[@id='column-a']")
elem2 =driver.find_element(By.XPATH, value="//*[@id='column-b']")
ActionChains(driver).drag_and_drop(elem1, elem2).perform()
time.sleep(2)
