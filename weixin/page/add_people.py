#from weixin.page.add_meber_page import AddMeberPage
from appium.webdriver.common.mobileby import MobileBy

from weixin.page.base_page import BasePage


class AddPeople(BasePage):
    '''
    添加成员详细页面
    '''
    # def __init__(self, driver):
    #     self.driver = driver
    ele_name =(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@class='android.widget.EditText']")

    def set_name(self, name):
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@class='android.widget.EditText']").send_keys(name)
        self.find_and_sedkeys(self.ele_name,name)
        return self

    def set_sex(self, sex):
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[contains(@text, '男')]").click()
        if sex == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '男')]").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        return self

    def set_phone(self, phone):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f8g").send_keys(phone)

        return self

    def click_save(self):
        from weixin.page.add_meber_page import AddMeberPage
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hi9").click()

        return AddMeberPage(self.driver)