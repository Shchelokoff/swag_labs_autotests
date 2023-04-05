import allure
from utilities.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.baseClass import Base

class FinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    selectProduct1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    cart = "//div[@id='shopping_cart_container']"
    mainWord = "//span[@class='title']"

    # Getters
    def getMainWord(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mainWord)))

    # Actions

    # Methods
    def finish(self):
        self.getCurrentURL()
        self.assertURL('https://www.saucedemo.com/checkout-complete.html')
        self.getScreenshot()
    def check(self):
        with allure.step("check"):
            Logger.add_start_step(method="check")
            print('We are on the finish page')
            self.assertURL('https://www.saucedemo.com/checkout-complete.html')
            self.assertWord(self.getMainWord(), 'Checkout: Complete!')
            Logger.add_end_step(url=self.driver.current_url, method="check")





