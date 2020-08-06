from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from time import sleep


class TestWC():
    def setup(self):
        des_apb={}
        des_apb['platformName']='android'
        des_apb['deviceName']= 'emulator-5554'
        des_apb['appPackage']= 'com.tencent.mm'
        des_apb['appActivity']= '.ui.LauncherUI'  #com.tencent.wework.launch.WwMainActivity
        des_apb['noReset']= 'true'
        des_apb['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
        des_apb['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
        # caps['dontStopAppOnReset'] = 'true'    # 启动之前不停止app
        des_apb['settings[waitForIdleTimeout]'] = 0


        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_apb)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_cases(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='汪亚秀 Amy']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='发消息']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.mm:id/aqg']").click()
        ele = self.driver.find_elements(MobileBy.XPATH, "//*[@resource-id='com.tencent.mm:id/a14']")
        ele[7].click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='发送']").click()


