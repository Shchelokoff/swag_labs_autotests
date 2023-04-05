from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.baseClass import Base
from utilities.logger import Logger


class LoginPage(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    userName = "//input[@id='user-name']"
    password = "//input[@id='password']"
    loginButton = "//input[@id='login-button']"
    mainWord = "//div[@class='login_logo']"

    # Getters
    def getUserName(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.userName)))
    def getPassword(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    def getLoginButton(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loginButton)))
    def getMainWord(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mainWord)))

    # Actions
    def inputUserName(self, userName):
        self.getUserName().send_keys(userName)
        print("Input login")
    def inputPassword(self, password):
        self.getPassword().send_keys(password)
        print("Input password")
    def clickLoginButton(self):
        self.getLoginButton().click()
        print("Click login button")

    # Methods
    def autorization(self):
        with allure.step("autorization"):
            Logger.add_start_step(method="autorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.inputUserName('standard_user')
            self.inputPassword('secret_sauce')
            self.clickLoginButton()
            Logger.add_end_step(url=self.driver.current_url, method="autorization")







