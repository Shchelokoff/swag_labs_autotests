import allure
from utilities.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.baseClass import Base

class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    selectProduct1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    selectProduct2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    selectProduct3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//div[@id='shopping_cart_container']"
    mainWord = "//span[@class='title']"
    menu = "//button[@id='react-burger-menu-btn']"
    linkAbout = "//a[@id='about_sidebar_link']"

    # Getters
    def getSelectProduct1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selectProduct1)))
    def getSelectProduct2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selectProduct2)))
    def getSelectProduct3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selectProduct3)))
    def getCart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    def getMainWord(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mainWord)))
    def getMenu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))
    def getLinkAbout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.linkAbout)))

    # Actions
    def clickSelectProducts1(self):
        self.getSelectProduct1().click()
        print("Select product1")
    def clickSelectProducts2(self):
        self.getSelectProduct2().click()
        print("Select product2")
    def clickSelectProducts3(self):
        self.getSelectProduct3().click()
        print("Select product3")
    def clickCart(self):
        self.getCart().click()
        print("Click cart")
    def clickMenu(self):
        self.getMenu().click()
        print("Click menu")
    def clickAboutPage(self):
        self.getLinkAbout().click()
        print("Go to the about page")

    # Methods
    def PushInCartProduct1(self):
        self.clickSelectProducts1()
        self.clickCart()
    def PushInCartProduct2(self):
        self.clickSelectProducts2()
        self.clickCart()
    def PushInCartProduct3(self):
        self.clickSelectProducts3()
        self.clickCart()
    def selectMenuAbout(self):
        self.clickMenu()
        self.clickAboutPage()
    def check(self):
        with allure.step("check"):
            Logger.add_start_step(method="check")
            print('We are on the main page')
            self.assertURL('https://www.saucedemo.com/inventory.html')
            self.assertWord(self.getMainWord(), 'Products')
            Logger.add_end_step(url=self.driver.current_url, method="check")




