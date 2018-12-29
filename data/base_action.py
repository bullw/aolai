import time
import allure
from selenium.webdriver.common.by import By


class Action():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc):
    # 在找元素之前 等待
        time.sleep(1)
        return self.driver.find_element(loc[0], loc[1])
    # 点击
    def click_element(self, loc):
        self.find_element(loc).click()
    # 向输入框输入内容
    def send_element_content(self, loc, content):
        self.find_element(loc).clear()
        time.sleep(1)
        self.find_element(loc).send_keys(content)



    #实现滑动业务
    def swipe_screen(self, tag):
        time.sleep(1)
        #获取当前手机窗口的大小
        screen_size = self.driver.get_window_size()
        width = screen_size.get("width") #获取手机宽
        height = screen_size.get("height")#获取手机的高
        if tag == 1:  # 向上滚动 两点之间滑动  x轴不变
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3, 1000)
        if tag == 2:  # 向下滚动
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, 1000)
        if tag == 3:  # 向左滚动
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, 1000)
        if tag == 4:  # 向右滚动
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5, 1000)

        # 获取吐司
    # def get_toast_text(self, t_ext):
    #     toast_xpath = "//*[contains(@text,'{}']".format(t_ext)
    #     toast_text = self.find_element((By.XPATH, toast_xpath)).text
    #     return toast_text
    def get_toast_text(self, message):
        # format 字符串位置映射
        toast_xpath = "//*[contains(@text,'{}')]".format(message)
        toast_message = self.find_element((By.XPATH, toast_xpath)).text
        return toast_message

    # 截图
    def get_screen(self):
        # png_name = "./screen/{}.png".format(int(time.strftime("%H:%M:%S")))
        # print(png_name)
        # self.driver.get_screenshot_as_png(png_name)
        png_name = "./screen/{}.png".format(int(time.time()))
        self.driver.get_screenshot_as_file(png_name)













