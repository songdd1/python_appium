import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

class BasePage():
    '''
    存放一些基础方法
    '''
    logging.basicConfig(level=logging.INFO)
    def __init__(self, driver:WebDriver=None):
        self.driver = driver

    def find(self, locator):
        return  self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_sedkeys(self, locator, text):
        self.find(locator).send_keys(text)

    def find_and_scoll(self, text):
       return self.driver.find_element(
                  MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          f'text("{text}").instance(0));')


    def bank(self, num=1):
        for i in range(num):
            self.driver.back()
