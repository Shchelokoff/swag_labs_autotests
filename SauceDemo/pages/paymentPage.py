import allure
from utilities.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.baseClass import Base

class PaymentPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    finishButton = "//button[@id='finish']"
    mainWord = "//span[@class='title']"

    # Getters
    def getFinishButton(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finishButton)))
    def getMainWord(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mainWord)))

    # Actions
    def clickfinishButton(self):
        self.getFinishButton().click()
        print("Click finish button")

    # Methods
    def payment(self):
        self.clickfinishButton()
    def check(self):
        with allure.step("check"):
            Logger.add_start_step(method="check")
            print('We are on the payment page')
            self.assertURL('https://www.saucedemo.com/checkout-step-two.html')
            self.assertWord(self.getMainWord(), 'Checkout: Overview')
            Logger.add_end_step(url=self.driver.current_url, method="check")




