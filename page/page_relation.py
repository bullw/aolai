from page.page_home import Home
from page.page_input import Input
from page.page_logined import Logined


class Relation_driver:
    # 初始化时 谁调用我,谁给我一个driver
    def __init__(self, driver):
        self.driver = driver

    def get_page_home(self):
        return Home(self.driver)

    def get_page_Input(self):
        return Input(self.driver)

    def get_page_Logined(self):
        return Logined(self.driver)