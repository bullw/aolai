import os, sys
sys.path.append(os.getcwd())
import time
import pytest
import yaml
from data.base_driver import driver_init
from page.page_relation import Relation_driver

data_list= []
with open(r"D:\就业班\pycharm\app_auto_day09\data\input_yaml.yaml", "r", encoding="utf-8") as f:
    data = yaml.load(f)
# print(data)
def read_yaml():
    for i in data.keys():
        data2 = data.get(i)
        # print(data2)
        username= data2.get("username")
        # print(username)
        password= data2.get("password")
        # print(password)
        tag = data2.get("tag")
        toast = data2.get("toast")
        correct_toast = data2.get("correct_toast")
        data_list.append((username,password, tag, toast, correct_toast))
        print(data_list)
    return data_list

class Test_login:

    app_all = ("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
    def setup_class(self):
        self.driver = driver_init(self.app_all)
        # 初始化导航对象
        self.bnal = Relation_driver(self.driver)

    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()

    #正确的
    # @pytest.mark.run(order=5)
    # def test_login(self):
    #     # 点击我的
    #     self.bnal.get_page_home().click_my()
    #     # 点击已有账号输入
    #     self.bnal.get_page_home().click_my_login()
    #     # 输入框输入(正确的情况)
    #     self.bnal.get_page_Input().login_kuang()
    #     # 点击登陆
    #     self.bnal.get_page_Input().click_login()
    #     #判断是否登录成功
    #     self.bnal.get_page_Logined().is_logined()
    #     # 点击设置,退出
    #     self.bnal.get_page_Logined().click_setting_back()

    @pytest.mark.parametrize('username, password, tag, toast, correct_toast', read_yaml())
    # @pytest.mark.run(order=10)
    @allure.step('登陆登出-异常处理')
    def test_login_error(self, username, password, toast, correct_toast, tag):
        # 点击我的
        allure.attach('描述', '点击我的')
        self.bnal.get_page_home().click_my()
        # 点击已有账号输入
        allure.attach('描述', '点击已有账号登录')
        self.bnal.get_page_home().click_my_login()
        allure.attach('描述', '输入账号密码')
        self.bnal.get_page_Input().login_kuang_error(username, password)
        allure.attach('描述', '点击登录')
        self.bnal.get_page_Input().click_login()
        if tag == 1:
            try:

                success_login = self.bnal.get_page_Logined().is_logined()
                # 点击设置, 退出
                self.bnal.get_page_Logined().click_setting_back()
                assert success_login,self.bnal.get_page_Input().get_screen()
            except:
                # 定位吐司
                self.bnal.get_page_Input().get_toast_text(toast)
                # 截图
                self.bnal.get_page_Input().get_screen()
                # 登录失败, 点击叉号
                self.bnal.get_page_Input().click_x()
        else:
            try:

                toast_meg = self.bnal.get_page_Input().get_toast_text(toast)
                allure.attach('描述', '截图')
                assert toast_meg == correct_toast, self.bnal.get_page_Input().get_screen()
            finally:
                allure.attach('描述', '点击x号')
                self.bnal.get_page_Input().click_x()



