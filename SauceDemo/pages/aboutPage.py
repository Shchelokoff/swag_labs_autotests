from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.baseClass import Base
from utilities.logger import Logger


class AboutPage(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    mainWord = "//span[@class='MuiTypography-root MuiTypography-buttonLabelNav css-1pj3is7']"

    # Getters
    def getMainWord(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mainWord)))

    # Actions

    # Methods
    def check(self):
        with allure.step("check"):
            Logger.add_start_step(method="check")
            print('We are on the about page')
            self.assertURL('https://saucelabs.com/')
            self.assertWord(self.getMainWord(), 'Products')
            Logger.add_end_step(url=self.driver.current_url, method="check")