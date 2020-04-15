import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from .page.index import Index


class TestTest:
    def setup_method(self):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_opts)
        self.driver.implicitly_wait(5)

    def test_test(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element(By.ID, 'check_corp_info').click()

    def teardown_method(self):
        self.driver.quit()


class TestAddMember:
    def setup_method(self):
        self.index = Index()

    def test_add_member(self):
        add_member = self.index.goto_add_member()
        # 添加成员
        add_member.add_member()
        time.sleep(3)
        # 测试是否添加
        assert add_member.get_first() == 'abcde'
