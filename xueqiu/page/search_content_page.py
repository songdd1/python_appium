from appium.webdriver.common.mobileby import MobileBy


from xueqiu.page.base_page import BasePage
from xueqiu.page.result_page import ResultPage


class SearchContentPage(BasePage):


    def iuput_content(self):
        ele = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']")
        self.find_and_sedkeys(ele, '小米')
        return ResultPage(self.driver)
