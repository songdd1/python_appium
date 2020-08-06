from appium import webdriver
from time import sleep


class TestWw():

    def setup(self):
        desired_caps = {
            'platformName': 'android',
            'platforVersion': '6.0',
            'browerName': 'Browser',
            'noRest': True,
            'deviceName': 'emulator-5554'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(10)


    def teardown(self):
        self.driver.quit()


    def test_case1(self):
        self.driver.get('http://m.baidu.com')