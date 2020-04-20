import time

import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
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

    @pytest.fixture(autouse=False)
    def driver_back_fixture(self):
        yield
        self.driver.back()

    @pytest.mark.parametrize('username, gender, tel', [
        (f'大黄狗{i}', i % 2, f'123{str(i)*8}') for i in range(1, 11)
    ])
    def test_add_user(self, driver_back_fixture, username, gender, tel):
        # 点击通讯录
        self.driver.find_element_by_xpath('//android.view.ViewGroup//*[@text="通讯录"]').click()
        # 滚动查找添加成员点击
        self.driver.find_element_by_android_uiautomator('new UiScrollable('
                                                        'new UiSelector().scrollable(true).instance(0))'
                                                        '.scrollIntoView(new UiSelector().text("添加成员")'
                                                        '.instance(0));').click()
        # 点击手动添加
        self.driver.find_element_by_id('com.tencent.wework:id/c56').click()
        time.sleep(2)
        # 验证添加联系人页面
        assert ".contact.controller.ContactAddActivity" in self.driver.current_activity

        # 输入姓名
        self.driver.find_element_by_xpath(
            '//*[contains(@text, "姓名")]/..//*[@resource-id="com.tencent.wework:id/ase"]'
        ).send_keys(username)
        # 选择性别
        self.driver.find_element_by_xpath('//*[@text="性别"]/..//*[@resource-id="com.tencent.wework:id/at7"]').click()
        if gender == 1:
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("男")').click()
        else:
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("男")').click()
        # 输入手机号
        self.driver.find_element_by_id('com.tencent.wework:id/emh').send_keys(tel)
        # 点击保存
        self.driver.find_element_by_id('com.tencent.wework:id/gq7').click()
        time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@text="添加成功"]')
        # assert "添加成功" in self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text

    @pytest.mark.parametrize('username', ['大黄狗', ])
    def test_delete_user(self, username):
        # 点击通讯录
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="通讯录"]').click()
        # 滚动查找
        user_els = self.driver.find_elements_by_android_uiautomator(
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0)).scrollIntoView('
            f'new UiSelector().textStartsWith("{username}").clickable(false).instance(0));')
        while len(user_els) > 0:
            user_els[0].click()
            # 点击三个竖点
            self.driver.find_element_by_id('com.tencent.wework:id/gq0').click()
            # 点击编辑成员
            self.driver.find_element_by_id('com.tencent.wework:id/axr').click()
            # 滑动点击删除成员, MuMu不滑动找不到
            self.driver.find_element_by_android_uiautomator(
                'new UiScrollable('
                'new UiSelector().scrollable(true).instance(0)).scrollIntoView('
                'new UiSelector().resourceId("com.tencent.wework:id/drk").instance(0));').click()
            # 点击确定
            self.driver.find_element_by_id('com.tencent.wework:id/b89').click()
            # 继续滚动查找点击, 这地方的f字符串"{username}"引号不能少
            user_els = self.driver.find_elements_by_android_uiautomator(
                'new UiScrollable('
                'new UiSelector().scrollable(true).instance(0)).scrollIntoView('
                f'new UiSelector().textStartsWith("{username}").clickable(false).instance(0));')
            # user_els = WebDriverWait(self.driver, 10).until(
            #     lambda driver: driver.find_elements_by_android_uiautomator(
            #         'new UiScrollable('
            #         'new UiSelector().scrollable(true).instance(0)).scrollIntoView('
            #         'new UiSelector().textStartsWith("大黄狗").clickable(false).instance(0));'
            #     )
            # )
        assert len(user_els) == 0

    @pytest.mark.parametrize('user', ['lao', 'da'])
    @pytest.mark.parametrize('msg', ['hi', '嗨'])
    def test_send_msg(self, driver_back_fixture, user, msg):
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

    def teardown_class(self):
        self.driver.quit()
