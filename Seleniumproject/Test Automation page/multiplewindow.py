from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
   
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://practice.expandtesting.com/windows")
driver.find_element(By.LINK_TEXT, value="Click Here").click()
time.sleep(2)
all_windows = driver.window_handles
original_window = all_windows[0]
driver.switch_to.window(original_window)
time.sleep(2)
driver.find_element(By.LINK_TEXT, value="Click Here").click()
time.sleep(2)
new_window = all_windows[-1]
driver.switch_to.window(new_window)
time.sleep(2)
driver.close()