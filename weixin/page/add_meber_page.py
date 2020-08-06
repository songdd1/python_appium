#from weixin.page.add_people import AddPeople
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from weixin.page.base_page import BasePage


class AddMeberPage(BasePage):
    '''
    添加成员
    '''
    # def __init__(self, driver):
    #     self.driver = driver
    ele_add = (MobileBy.ID, 'com.tencent.wework:id/hqb')

    def add_input(self):
        from weixin.page.add_people import AddPeople
        # self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hqb').click()
        self.find_and_click(self.ele_add)
        return AddPeople(self.driver)

    def get_toast(self):
        tex = WebDriverWait(self.driver, 10).until(lambda x:x.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']")).text
        return tex

