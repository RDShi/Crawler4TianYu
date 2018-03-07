from utils import *


if __name__ == '__main__':
    driver = init_driver()
    handle_login(driver)
    goto_download_page(driver)
    name_list = ["史润东", "杜远超", "田雨"]
    #截止时间（不含），格式年，月，日（，时，分，秒）
    time_end = datetime(2018, 3, 6)
    #起始时间（含）
    time_start = datetime(2018, 2, 1)
    #下载数据
    for name in name_list:
        download(driver, name, time_end, time_start)
    driver.close()
    # driver.quit()