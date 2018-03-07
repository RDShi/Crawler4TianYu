"""utils"""
import os
from time import sleep
from datetime import datetime
import csv
from selenium import webdriver
WAIT_TIME = 1


def init_driver():
    """初始化配置"""
    chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chrome_driver
    drv = webdriver.Chrome(chrome_driver)
    return drv


def handle_login(driver):
    """执行登录"""
    # 定义自己的用户名密码
    username = "qf"
    password = "qf123"
    # 执行操作的页面地址
    login_url = "http://10.1.102.251/a/login"
    driver.set_window_size(480, 760)
    driver.get(login_url)
    # cookie1 = driver.get_cookies()# 获得cookie信息
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name("btn").click()


def goto_download_page(driver):
    """进入数据页面"""
    # 进入历史记录
    driver.find_element_by_xpath("// *[ @ id ='menu-6081261d798f44f8be07a5f7c6c75f8d']"
                                 "/div[3]/div[1]/a").click()
    # 进入用户记录
    sleep(WAIT_TIME)
    driver.find_element_by_xpath("//*[@id='collapse-28db4d4a824c4d4cae9405e0d9e4d1ba']"
                                 "/div/ul/li[1]/a").click()

    #关闭员工管理小窗口
    sleep(WAIT_TIME)
    driver.find_element_by_xpath("//*[@id ='jerichotab_0']/div[1]/div[2]/a").click()
    #定位iframe并切进去
    sleep(WAIT_TIME)
    driver.switch_to.frame("jerichotabiframe_1")


def download(driver, name, time_end, time_start):
    """执行下载"""
    #输入名字
    sleep(WAIT_TIME)
    elem = driver.find_element_by_id("name")
    elem.clear()
    elem.send_keys(name)
    #点击查询
    sleep(WAIT_TIME)
    driver.find_element_by_xpath("//*[@id ='btnSubmit']").click()
    #内容
    #文字内容，并记录为csv
    fid = open(name+".csv", "w", newline="")
    writer = csv.writer(fid)
    sleep(WAIT_TIME)
    #点击第一页
    try:
        driver.find_element_by_xpath("/html/body/div/ul/li[2]/a").click()
    except:
        print("点击第一页出错")

    i = 1
    while 1:
        try:
            if i == 1:
                sleep(WAIT_TIME)
            text_cont = driver.find_element_by_xpath("//*[@id='contentTable']/tbody/tr["
                                                     +str(i)+"]/td[8]").text
            time = text_cont.split()
            date = time[0].split('-')
            moment = time[1].split(':')
            record_time = datetime(int(date[0]), int(date[1]), int(date[2]),
                                   int(moment[0]), int(moment[1]), int(moment[2]))
            print(record_time)
            i = i + 1
            if record_time > time_end:
                continue
            if record_time < time_start:
                fid.close()
                return
            print(name, record_time)
            writer.writerow([str(record_time)])
        except:
            try:
                # 下一页
                sleep(WAIT_TIME)
                i = 1
                driver.find_element_by_xpath("//a[contains(text(),'下一页')]").click()
            except:
                print("起始时间超出范围，或者姓名不存在")
                fid.close()
                return
