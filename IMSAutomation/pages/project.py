from selenium.webdriver.common.by import By

class ProjectPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_txtbox = (By.ID, "username")
        self.password_txtbox = (By.ID, "password")
        self.login_button = (By.XPATH, '//*[@id="login-form"]/div/div[2]/div[4]/input')
        self.search_txtbox = (By.ID, "project-title")
        self.filter_field = (By.XPATH, "//span[text()='Filters']")
        self.import_button = (By.XPATH, '//*[contains(@href,"/projects/import")]')
        self.addproject_button = (By.XPATH, '//*[contains(@href,"/projects/create")]')
        self.nepali_convert= (By.XPATH, "//span[text()='ने']")
        self.english_convert= (By.XPATH, "//span[text()='en']")
        self.filter_option= (By.XPATH,'//*[@class="trigger"]')
        self.radio1_option= (By.XPATH,'//input[@value="pipeline"]')
        self.radio2_option= (By.XPATH,'//input[@value="implementation"]')
        self.radio3_option= (By.XPATH,'//input[@value="completion"]')
        self.radio4_option= (By.XPATH,'//input[@value="cancelled"]')
        self.social_option= (By.XPATH,'//*[@class="tabs__item uppercase is-active"]')


    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_txtbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_txtbox).send_keys(password)
         
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def search_field(self, search):
        self.driver.find_element(*self.search_txtbox).send_keys(search)
    
    def filter_box(self):
        self.driver.find_element(*self.filter_field).click()
         
    def import_project(self):
        self.driver.find_element(*self.import_button).click()

    def add_project(self):
        self.driver.find_element(*self.addproject_button).click()
    
    def nepali_con(self):
        self.driver.find_element(*self.nepali_convert).click()
    
    def english_con(self):
        self.driver.find_element(*self.english_convert).click()
    
    def filter_button(self):
        self.driver.find_element(*self.filter_option).click()
    
    def radio_opt1(self):
        self.driver.find_element(*self.radio1_option).click()
    
    def radio_opt2(self):
        self.driver.find_element(*self.radio2_option).click()
    
    def radio_opt3(self):
        self.driver.find_element(*self.radio3_option).click()
    
    def radio_opt4(self):
        self.driver.find_element(*self.radio4_option).click()
    
    def add_project(self):
        self.driver.find_element(*self.addproject_button).click()

    def import_project(self):
        self.driver.find_element(*self.import_button).click()
    
    def project_social(self):
        self.driver.find_element(*self.social_option).click()
        

   

