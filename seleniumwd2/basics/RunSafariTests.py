from selenium import webdriver
import os

class RunSafariTests():
    # https://github.com/SeleniumHQ/selenium/wiki/SafariDriver
    # http://selenium-release.storage.googleapis.com/index.html

    def test(self):
        serverLocation = "C:\\Users\\rreyes.FARM\\AppData\\Local\\Programs\\Python\\Python35-32\\libs\\selenium-server-standalone-2.53.0.jar"
        os.environ["SELENIUM_SERVER_JAR"] = serverLocation
        # Instantiate Safari Browser Command
        driver = webdriver.Safari(quiet=True)
        # Open the provided URL
        driver.get("http://www.letskodeit.com")

safari = RunSafariTests()
safari.test()
