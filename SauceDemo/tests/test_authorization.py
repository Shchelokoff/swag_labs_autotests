import time
import allure
from pages.loginPage import LoginPage
from pages.mainPage import MainPage

@allure.description("test_authorization")
def test_authorization(driver):
    log = LoginPage(driver)
    log.autorization()
    mp = MainPage(driver)
    mp.check()
    time.sleep(5)