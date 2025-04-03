from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_button = (By.ID, "login2")
        self.username_field = (By.ID, "loginusername")
        self.password_field = (By.ID, "loginpassword")
        self.submit_button = (By.XPATH, "//button[text()='Log in']")

    def open_login_modal(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.submit_button).click()
