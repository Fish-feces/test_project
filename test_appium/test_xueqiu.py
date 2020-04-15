from appium import webdriver


desired_caps = {
    "platformName": "android",
    "deviceName": "emulator-5554",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "noReset": "true",
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

