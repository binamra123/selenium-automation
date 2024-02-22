from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
   
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://practice.expandtesting.com/login")
print(driver.current_url)
print(driver.title)
driver.maximize_window()
driver.fullscreen_window()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.find_element(By.XPATH, value="//div[@id='main-navbar']/ul[1]/li[2]/a").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
driver.quit()

