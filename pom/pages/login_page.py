from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self,driver):   #constructor
        self.driver = driver
        self.username_txtbox = '(By.ID, value="username")'
        self.password_txtbox = '(By.ID, value="password")'
        self.login_button = '''(By.XPATH, value="//button[@class='btn btn-bg btn-primary d-block w-100']")'''


    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_txtbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_txtbox).send_keys(password)
         
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

