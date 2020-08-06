from appium.webdriver.common.mobileby import MobileBy

from xueqiu.page.base_page import BasePage
from xueqiu.page.search_page import SearchPage


class ResultPage(BasePage):

    def select_content(self):

        ele = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/code' and @text='BK0611']/../..")
        self.find_and_click(ele)
        return SearchPage(self.driver)