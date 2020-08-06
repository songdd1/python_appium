from appium.webdriver.common.mobileby import MobileBy

from xueqiu.page.base_page import BasePage
from xueqiu.page.market_page import  MarketPage


class MainPage(BasePage):

    def go_to_market(self):
        ele =(MobileBy.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']")
        self.find_and_click(ele)
        return MarketPage(self.driver)

