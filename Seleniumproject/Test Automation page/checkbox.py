from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
   
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://practice.expandtesting.com/#examples")
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

element = driver.find_element(By.XPATH, value="//*[@id='examples']/div[8]/div[2]/div/div/h3/a");
ActionChains(driver).move_to_element(element).click().perform()
time.sleep(2)
driver.find_element(By.ID, value="checkbox1").click()
driver.find_element(By.ID, value="checkbox2").click()
check1 = driver.find_element(By.ID, value="checkbox1").is_selected()
check2 = driver.find_element(By.ID, value="checkbox2").is_selected()
print(check1)
print(check2)