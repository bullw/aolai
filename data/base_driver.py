from appium import webdriver


def driver_init(app):

    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.170.101:5555'
    # 获取Toast
    desired_caps['automationName'] = 'Uiautomator2'
    # app信息
    desired_caps['appPackage'] = app[0]
    desired_caps['appActivity'] = app[1]
    # 中文声明
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)