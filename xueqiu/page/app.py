from appium import webdriver

from xueqiu.page.base_page import BasePage
from xueqiu.page.main_page import MainPage


class App(BasePage):

    def stat(self):
        if self.driver == None:
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

            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_apb)
        else:
            self.driver.launch_app()

        self.driver.implicitly_wait(10)

    def restat(self):
        self.driver.close()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def go_to_main(self):
        return MainPage(self.driver)
