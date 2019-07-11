from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    def __init__(self):
        desired_caps = {}

        # 解决中文问题
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app信息
        desired_caps['appPackage'] = 'com.vcooline.aike'
        desired_caps['appActivity'] = '.umanager.LoginActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def base_find(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_element(*loc))

    def base_input(self, loc, value):
        el = self.base_find(loc)
        el.clear()
        el.send_keys(value)

    def base_click(self, loc):
        self.base_find(loc).click()
