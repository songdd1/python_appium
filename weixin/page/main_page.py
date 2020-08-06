from appium.webdriver.common.mobileby import MobileBy

from weixin.page.base_page import BasePage
from weixin.page.team_page import TeamPage


class MainPage(BasePage):
    '''
    主页面
    '''
    # def __init__(self, driver):
    #     self.driver = driver
    ele_team = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/e48'and @text='团队']")

    def go_to_teamlist(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/e48'and @text='团队']").click()
        self.find_and_click(self.ele_team)
        return TeamPage(self.driver)

    def go_to_msg(self):
        pass