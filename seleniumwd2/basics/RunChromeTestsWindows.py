from selenium import webdriver
import os

class RunChromeTestsWindows():
    # https://sites.google.com/a/chromium.org/chromedriver/downloads
    # http://chromedriver.storage.googleapis.com/index.html?path=2.21/
    def test(self):
        driverLocation = "C:\\Users\\rreyes.FARM\\AppData\\Local\\Programs\\Python\\Python35-32\\libs\\chromedriver.exe" #code for Chrome only
        os.environ["webdriver.chrome.driver"] = driverLocation #code for Chrome only
        driver = webdriver.Chrome(driverLocation)
        driver.get("http://www.letskodeit.com")

chromeTest = RunChromeTestsWindows()
chromeTest.test()
