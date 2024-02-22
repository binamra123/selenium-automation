from selenium.webdriver.common.by import By

class SignupPage:

    def __init__(self,driver):   #constructor
        self.driver = driver
        self.number_txtbox = '''(By.XPATH, value="//input[@id='input-number']")'''
        self.text_txtbox = '''(By.XPATH, value="//input[@id='input-text']")'''
        self.password_txtbox = '''(By.XPATH, value="//input[@id='input-password']")'''
        self.date_txtbox = '''(By.XPATH, value="//input[@id='input-date']")'''
        self.display_button = '''(By.XPATH, value="//button[@id='btn-display-inputs']")'''
        self.clear_button = '''(By.XPATH, value="///button[@id='btn-clear-inputs']")'''


    def open_page(self, url):
        self.driver.get(url)

    def enter_number(self, number):
        self.driver.find_element(self.number_txtbox).send_keys(number)

    def enter_text(self, text):
        self.driver.find_element(self.text_txtbox).send_keys(text)
    
    def enter_password(self, password):
        self.driver.find_element(self.password_txtbox).send_keys(password)

    def enter_date(self, date):
        self.driver.find_element(self.datw).send_keys(password)
    
    def click_display(self):
        self.driver.find_element(self.display_button).click()

    def click_clear(self):
        self.driver.find_element(self.clear_button_button).click()

