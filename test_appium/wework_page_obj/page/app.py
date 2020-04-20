from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _black_list = [
        (MobileBy.XPATH, '//*[@text="确定"]'),
        (MobileBy.XPATH, '//*[@text="允许"]')
    ]

    _error_num = 0
    _error_max = 3
    _param = {}

    def __init__(self, driver: WebDriver=None):
        self._driver = driver

    def find(self, locator, value):
        try:
            return self._driver.find_element(*locator) if isinstance(locator, tuple) \
                else self._driver.find_element(locator, value)
        except Exception as e:
            if self._error_num > self._error_max:
                raise e
            self._error_num += 1
            # 处理弹框
            for ele in self._black_list:
                el_list = self._driver.find_elements(*ele)
                if len(el_list) > 0:
                    el_list[0].click()
                    self.find(locator, value)
            raise e


class App(BasePage):
    def start(self):
        # 启动 app
        caps = {
            'platformName': 'android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.WwMainActivity',
            'noReset': 'true'
        }
        self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self._driver.implicitly_wait(5)
        return self

    def main(self):
        from .main import Main
        return Main(self._driver)
