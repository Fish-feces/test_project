from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver=None):
        self.driver = None
        if driver is None:
            opts = webdriver.ChromeOptions()
            opts.debugger_address="127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opts)
            self.driver.implicitly_wait(3)
        else:
            self.driver = driver
