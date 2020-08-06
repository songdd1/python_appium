import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

with open('../../weixin/data/datas.yml') as f:
    addcon = yaml.safe_load(f)


class TestContact():

    def setup_class(self):
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
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/e48'and @text='团队']").click()
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize('name,sex,phonenum',addcon)
    def test_case1(self,name,sex, phonenum):
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/e48'and @text='团队']").click()
        #点击添加成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员...']").click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hqb').click()
        sleep(3)
        #输入姓名
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@class='android.widget.EditText']").send_keys(name)
        #输入性别
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[contains(@text, '男')]").click()
        if sex == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '男')]").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        #输入手机号码
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f8g").send_keys(phonenum)
        #点击保存
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hi9").click()
        #显示等待toast元素
        ele = WebDriverWait(self.driver, 10).until(lambda x:x.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        #ele = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text

        assert '成功' in ele.text
        self.driver.back()

