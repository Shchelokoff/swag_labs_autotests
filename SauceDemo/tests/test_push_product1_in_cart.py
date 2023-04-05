import time
import allure
from pages.cartPage import CartPage
from pages.loginPage import LoginPage
from pages.mainPage import MainPage

@allure.description("test_buy_product1")
def test_buy_product1(driver):
    log = LoginPage(driver)
    log.autorization()
    mp = MainPage(driver)
    mp.check()
    mp.PushInCartProduct1()
    cp = CartPage(driver)
    cp.check()
    time.sleep(5)