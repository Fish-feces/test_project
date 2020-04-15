import pytest
from appium import webdriver


class TestWEWork:
    def setup_method(self):
        desired_caps = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": "true",
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    @pytest.mark.parametrize('user', ['dahuanggou', ])
    @pytest.mark.parametrize('msg', ['en'])
    def test_send_msg(self, user, msg):
        import time
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.TextView').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.tencent.wework:id/gq_').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.tencent.wework:id/ffq').send_keys(user)
        time.sleep(3)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.tencent.wework:id/aaj').click()
        time.sleep(3)
        el = self.driver.find_element_by_id('com.tencent.wework:id/dtv')
        el.click()
        el.send_keys(msg)
        self.driver.find_element_by_id('com.tencent.wework:id/dtr').click()
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
