from appium import webdriver
from time import sleep


class TestXq():

    def setup(self):
        desired_caps = {}
        desired_caps['platformName']='android'
        desired_caps['deviceName']='emulator-5554'
        desired_caps['appPackage']='com.xueqiu.android'
        desired_caps['appActivity']='.common.MainActivity'
        desired_caps['noReset']='true'
        desired_caps['skipDeviceInitialization']='true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(10)


    def teardown(self):
        self.driver.quit()


    def test_case1(self):
        self.driver.find_element_by_id('com.weixin.android:id/tv_search').click()
        self.driver.find_element_by_id('com.weixin.android:id/search_input_text').send_keys('alibaba')
        self.driver.find_element_by_xpath("//*[@resource-id='com.weixin.android:id/name' and @text='阿里巴巴']").click()
        sleep(2)


    def test_case2(self):
        ele = self.driver.find_element_by_id('com.weixin.android:id/tv_search')
        search_enable = ele.is_enabled()
        print(ele.text)
        print(ele.location)
        print(ele.size)
        if search_enable == True:
            ele.click()
            self.driver.find_element_by_id('com.weixin.android:id/search_input_text').send_keys('alibaba')
            alibaba_ele= self.driver.find_element_by_xpath("//*[@resource-id='com.weixin.android:id/name' and @text='阿里巴巴']")
            print(alibaba_ele.get_attribute("displayed"))


    def test_case3(self):
        self.driver.find_element_by_id('com.weixin.android:id/tv_search').click()
        self.driver.find_element_by_id('com.weixin.android:id/search_input_text').send_keys('alibaba')
        self.driver.find_element_by_xpath("//*[@resource-id='com.weixin.android:id/name' and @text='阿里巴巴']").click()




