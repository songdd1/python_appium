from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver



class BasePage():

    def __init__(self, driver:WebDriver=None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_sedkeys(self, locator, text):
        self.find(locator).send_keys(text)

    def find_and_scrool(self, locator):
        pass
