from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
   
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://practice.expandtesting.com/#examples")
driver.find_element(By.XPATH, value="//*[@id='examples']/div[2]/div[2]/div/div/h3/a").click()
driver.find_element(By.ID, value="blue").click()
time.sleep(2)
driver.find_element(By.ID, value="red").click()
time.sleep(2)
driver.find_element(By.ID, value="yellow").click()
time.sleep(2)
driver.find_element(By.ID, value="black").click()
driver.close()