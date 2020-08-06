from appium.webdriver.common.mobileby import MobileBy

from weixin.page.add_meber_page import AddMeberPage
from weixin.page.base_page import BasePage
from weixin.page.my_page import MyPage


class TeamPage(BasePage):
    '''
    团队页面
    '''
    # def __init__(self, driver):
    #     self.driver = driver
    ele_add = (MobileBy.XPATH, "//*[@text='添加成员...']")

    def add_contact(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员...']").click()
        self.find_and_click(self.ele_add)
        return AddMeberPage(self.driver)

    def search_contact(self):
        return

    def go_to_my(self):
        return MyPage()