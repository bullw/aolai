from data.base_action import Action
import data
import allure
class Logined(Action):

    def __init__(self, driver):
        Action.__init__(self, driver)

    # 通过能否定位到用户名的位置来判断是否登陆成功
    @allure.step('判断是否登录成功')
    def is_logined(self):
        try:
            self.find_element(data.logined_username)
            print("\nIs ok!")
            return True
        except:
            return False

    # 点击设置 退出
    @allure.step('登出')
    def click_setting_back(self):
        allure.attach('描述', '点击设置')
        self.click_element(data.logined_setting)
        allure.attach('描述', '上滑动')
        self.swipe_screen(1)
        allure.attach('描述', '点击退出')
        self.click_element(data.setting_quit)
        allure.attach('描述', '点击删除')
        self.click_element(data.setting_delete)