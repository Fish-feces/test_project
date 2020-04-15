import pytest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException


class TestWEWork:
    def setup_class(self):
        desired_caps = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": "true",
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    @pytest.mark.parametrize('user', ['lao', 'da'])
    @pytest.mark.parametrize('msg', ['hi', '嗨'])
    def test_send_msg(self, user, msg):
        # 点击通讯录
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="通讯录"]').click()
        # 点击搜索
        self.driver.find_element_by_id('com.tencent.wework:id/gq_').click()
        # 输入搜索关键字
        self.driver.find_element_by_id('com.tencent.wework:id/ffq').send_keys(user)
        # 点击联系人搜索结果第一个
        try:
            self.driver.find_element_by_xpath(
                '//android.widget.TextView[@text="联系人"]/../following-sibling::android.widget.RelativeLayout[1]'
            ).click()
        except NoSuchElementException:
            print(f'联系人搜索结果为空, 输入内容: {user}')
            return
        # 点击发送消息
        self.driver.find_element_by_id('com.tencent.wework:id/aaj').click()
        # 输入消息
        self.driver.find_element_by_id('com.tencent.wework:id/dtv').send_keys(msg)
        # 点击发送
        self.driver.find_element_by_id('com.tencent.wework:id/dtr').click()

    def teardown_method(self):
        self.driver.back()

    def teardown_class(self):
        self.driver.quit()
