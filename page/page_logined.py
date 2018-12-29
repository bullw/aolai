from data.base_action import Action
import data

class Logined(Action):

    def __init__(self, driver):
        Action.__init__(self, driver)

    # 通过能否定位到用户名的位置来判断是否登陆成功
    def is_logined(self):
        try:
            self.find_element(data.logined_username)
            print("\nIs ok!")
            return True
        except:
            return False

    # 点击设置
    def click_setting_back(self):
        self.click_element(data.logined_setting)
        self.swipe_screen(1)
        self.click_element(data.setting_quit)
        self.click_element(data.setting_delete)