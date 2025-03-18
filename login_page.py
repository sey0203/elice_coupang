from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from tests.coupang import password
import time

class LoginPage():
    URL = "https://login.coupang.com/login/login.pang?rtnUrl=https%3A%2F%2Fwww.coupang.com%2Fnp%2Fpost%2Flogin%3Fr%3Dhttps%253A%252F%252Fwww.coupang.com%252F"
    EMAIL_INPUT_ID = "login-email-input"
    PASSWORD_INPUT_ID = "login-password-input"
    LOGIN_EMAIL = password.email
    LOGIN_PASSWORD = password.password

    
    def __init__(self, driver: WebDriver):
        self.driver = driver

    #로그인페이지 열기
    def open(self):
        self.driver.get(self.URL)

    def login_success(self):
        login_email_input = self.driver.find_element(By.ID, self.EMAIL_INPUT_ID)
        login_email_input.send_keys(self.LOGIN_EMAIL)

        time.sleep(3)

        login_password_input = self.driver.find_element(By.ID, self.PASSWORD_INPUT_ID)
        login_password_input.send_keys(self.LOGIN_PASSWORD)

        time.sleep(3)

        login_password_input.send_keys(Keys.ENTER)