from appium.webdriver.common.mobileby import MobileBy

from .app import BasePage
from .address_list import AddressListPage


class Main(BasePage):
    def click_address_list(self):
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self._driver)
