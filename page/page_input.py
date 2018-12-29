import time

import pytest
import allure
import data
from data.base_action import Action

class Input(Action):

    def __init__(self, driver):
        Action.__init__(self, driver)

    # 账号框输入
    def login_kuang(self):
        self.send_element_content(data.un_kuang, "18406500469")
        self.send_element_content(data.pw_kuang, "123456")

    # 各种 error
    def login_kuang_error(self, username, password):
        self.send_element_content(data.un_kuang, username)
        self.send_element_content(data.pw_kuang, password)

    # 点击登陆
    def click_login(self):
        self.click_element(data.login_in)

    # 吐司判断
    def is_toast_error(self):
        try:
            self.find_element(data.toast_login)
            return True
        except:
            return False

    # 吐司判断 通过是否可以定位到判断
    def is_toast_no(self):
        self.find_element(data.toast_login_no)

    #　右上角的ｘ号
    def click_x(self):
        self.click_element(data.login_x)
