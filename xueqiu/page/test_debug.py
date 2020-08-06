from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestA():

    def setup(self):
        des_apb = {}
        des_apb['platformName'] = 'android'
        des_apb['deviceName'] = 'emulator-5554'
        des_apb['appPackage'] = 'com.xueqiu.android'
        des_apb['appActivity'] = '.common.MainActivity'  # com.tencent.wework.launch.WwMainActivity
        des_apb['noReset'] = 'true'
        des_apb['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
        des_apb['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
        # caps['dontStopAppOnReset'] = 'true'    # 启动之前不停止app
        des_apb['settings[waitForIdleTimeout]'] = 0
        des_apb['dontStopAppOnReset'] = 'true'
        # des_apb['unicodeKeyboard'] = 'true'
        # des_apb['resetKeyboard'] = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_apb)
        self.driver.implicitly_wait(10)


    def test_case1(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/home_search']").click()
        sleep(2)
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys('alibaba')
        #self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").click()
        #self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/code' and @text='BK2525']/..").click()
        #self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']/../..").click()
        sleep(5)