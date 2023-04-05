import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver
# Method get current url
    def getCurrentURL(self):
        getURL = self.driver.current_url
        print("Current URL " + getURL)
# Method assert word "Product"
    def assertWord(self, word, result):
        valueWord = word.text
        assert valueWord == result
        print("Text main word is right")
# Method screenshot
    def getScreenshot(self):
        nowDate = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        nameScreenshot = 'screenshot' + nowDate + '.png'
        self.driver.save_screenshot('C:\\Users\\shche\\PycharmProjects\\SauceDemo\\screen\\' + nameScreenshot)
# Method assert URL
    def assertURL(self, result):
        getURL = self.driver.current_url
        print(getURL)
        assert getURL == result
        print("URL of the current page is right")



