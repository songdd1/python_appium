from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from time import sleep


class TestWC():
    def setup(self):
        des_apb={}
        des_apb['platformName']='android'
        des_apb['deviceName']= 'emulator-5554'
        des_apb['appPackage']= 'com.tencent.wework'
        des_apb['appActivity']= '.launch.LaunchSplashActivity'  #com.tencent.wework.launch.WwMainActivity
        des_apb['noReset']= 'true'
        des_apb['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
        des_apb['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
        # caps['dontStopAppOnReset'] = 'true'    # 启动之前不停止app
        des_apb['settings[waitForIdleTimeout]'] = 0


        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_apb)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_case1(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="工作台"]').click()
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/h58').click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text, '次外出')]").click()

    def test_case2(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="团队"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hib').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/g5b').send_keys('sdd1')
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/dd4"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hi2').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b4g" and@text="编辑成员"]').click()
