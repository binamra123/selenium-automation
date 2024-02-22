from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
   
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.leapwork.com/services/learning-center/testing-internet-hovers")
hoverele = driver.find_element(By.XPATH, value="//a[normalize-space()='Product']")
action_chains = ActionChains(driver)
action_chains.move_to_element(hoverele).perform()
time.sleep(2)
driver.find_element(By.XPATH, value="//*[@id='hs_cos_wrapper_module_168233503200118']/div/div/div/div/div/div[2]/div/div/div/div[1]/ul/li[2]/a/div/div/div/div[2]/h6").click()
time.sleep(2)