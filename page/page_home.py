from data.base_action import Action
import data
import allure
import os, sys
sys.path.append(os.getcwd())
"""
登陆的业务逻辑
"""

class Home(Action):
    # 初始化对象
    def __init__(self, driver):
        Action.__init__(self, driver)
    # 首页点击我的
    def click_my(self):
        self.click_element(data.my)
    """
    点击已有账号登陆
    
    """
    def click_my_login(self):
        self.click_element(data.my_login)

