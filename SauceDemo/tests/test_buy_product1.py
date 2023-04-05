import time
import allure
from pages.cartPage import CartPage
from pages.customerInfoPage import CustomerInfoPage
from pages.finishPage import FinishPage
from pages.loginPage import LoginPage
from pages.mainPage import MainPage
from pages.paymentPage import PaymentPage

@allure.description("test_buy_product1")
def test_buy_product1(driver):
    log = LoginPage(driver)
    log.autorization()
    mp = MainPage(driver)
    mp.check()
    mp.PushInCartProduct1()
    cp = CartPage(driver)
    cp.check()
    cp.clickCheckoutButton()
    cip = CustomerInfoPage(driver)
    cip.check()
    cip.inputCustomerInfo()
    p = PaymentPage(driver)
    p.check()
    p.clickfinishButton()
    f = FinishPage(driver)
    f.check()
    time.sleep(5)