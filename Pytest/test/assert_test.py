from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
   
def test_assert():
 driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
 driver.get("https://practice.expandtesting.com/login")
 expected_title = 'Test Automation Practice: Working with Login '
 actual_title = driver.title
 assert actual_title == expected_title
 driver.find_element(By.XPATH, value="//input[@id='username']").send_keys('practice')
 driver.find_element(By.XPATH, value="//input[@id='password']").send_keys('SuperSecretPassword!')
 driver.find_element(By.XPATH, value="//button[@class='btn btn-bg btn-primary d-block w-100']").click()
