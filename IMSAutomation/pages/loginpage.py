from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_txtbox = (By.ID, "username")
        self.password_txtbox = (By.ID, "password")
        self.login_button = (By.XPATH, '//*[@id="login-form"]/div/div[2]/div[4]/input')

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_txtbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_txtbox).send_keys(password)
         
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
