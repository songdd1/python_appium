from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from xueqiu.page.base_page import BasePage
from xueqiu.page.search_content_page import SearchContentPage


class MarketPage(BasePage):
    def search_content(self):
        ele = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
       # WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(ele))

        self.find_and_click(ele)
        return SearchContentPage(self.driver)