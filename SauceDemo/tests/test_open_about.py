import allure
import time
from pages.aboutPage import AboutPage
from pages.loginPage import LoginPage
from pages.mainPage import MainPage

@allure.description("test_open_about")
def test_open_about(driver):
    log = LoginPage(driver)
    log.autorization()
    mp = MainPage(driver)
    mp.check()
    mp.selectMenuAbout()
    ap = AboutPage(driver)
    ap.check()
    time.sleep(5)
