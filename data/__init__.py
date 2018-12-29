from selenium.webdriver.common.by import By


"""
首页 分类  购物车 我
"""
home = By.ID, "com.yunmall.lc:id/tab_home"
fenlei = By.ID, "com.yunmall.lc:id/tab_category"
gouwuche = By.ID, "com.yunmall.lc:id/tab_shopping_cart"
my = By.ID, "com.yunmall.lc:id/tab_me"

"""
我的
"""
# 已有账号登陆
my_login = By.ID, "com.yunmall.lc:id/textView1"

"""
定位账号i输入框 登录按钮
"""
un_kuang = By.ID, "com.yunmall.lc:id/logon_account_textview"
pw_kuang = By.ID, "com.yunmall.lc:id/logon_password_textview"
login_in = By.ID, "com.yunmall.lc:id/logon_button"
# 右上角的x号
login_x = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_layout"


"""
登录成功后用户名定位 设置
"""
logined_username = By.ID, "com.yunmall.lc:id/tv_user_nikename"
logined_setting = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

"""
设置中退出
"""
setting_quit = By.ID, "com.yunmall.lc:id/setting_logout"
"""
点击退出后 确认删除键
"""
setting_delete = By.ID, "com.yunmall.lc:id/ymdialog_right_button"

"""
土司定位
"""
toast_login = By.XPATH, "//*[contains(@text, '登录密码错误')]"
toast_login_no = By.XPATH, "//*[contains(@text, '不存在')]"