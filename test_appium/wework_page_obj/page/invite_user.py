from appium.webdriver.common.mobileby import MobileBy

from .app import BasePage
from .manual_add_form import ManualAddFormPage


class InviteUserPage(BasePage):
    # 手动添加
    def click_manual_add(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/c56").click()
        return ManualAddFormPage(self._driver)

    def click_back(self):
        self._driver.back()
        from .address_list import AddressListPage
        return AddressListPage(self._driver)

    def get_verify_toast(self):
        return self, self.find(MobileBy.XPATH, "//*[@text='添加成功']")
