from appium.webdriver.common.mobileby import MobileBy

from .app import BasePage
from .invite_user import InviteUserPage


class AddressListPage(BasePage):
    def click_add_user(self):
        # 滚动查找 添加成员
        self.find(
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView(new UiSelector().text("添加成员")'
            '.instance(0));').click()
        return InviteUserPage(self._driver)
