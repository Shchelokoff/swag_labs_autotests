import allure
from utilities.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.baseClass import Base

class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    checkoutButton = "//button[@id='checkout']"
    mainWord = "//span[@class='title']"

    # Getters
    def getCheckoutButton(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkoutButton)))
    def getMainWord(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mainWord)))

    # Actions
    def clickCheckoutButton(self):
        self.getCheckoutButton().click()
        print("Click checkout button")

    # Methods
    def productConfirmation (self):
        self.getCurrentURL()
        self.clickCheckoutButton()
    def check(self):
        with allure.step("check"):
            Logger.add_start_step(method="check")
            print('We are on the cart page')
            self.assertURL('https://www.saucedemo.com/cart.html')
            self.assertWord(self.getMainWord(), 'Your Cart')
            Logger.add_end_step(url=self.driver.current_url, method="check")




