# -*- coding: utf-8 -*-


#爬取51job的信息

import re
import xlwt
import sqlite3
from selenium import webdriver
import time
import analysis_data
import ope_xls
import ope_sqlite

#生成驱动
fire_opts = webdriver.FirefoxOptions()
fire_opts.set_preference("permissions.default.image", 2)
driver = webdriver.Firefox()

datalist = []
#循环发送请求并且获得数据
def get_datalist():
    driver.get("http://www.baidu.com")
    time.sleep(3)
    for i in range(1, 51):
        url = "https://search.51job.com/list/000000,000000,0000,00,9,99,Java%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,"+str(i)+".html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
        driver.get(url)
        time.sleep(3)
        elem = driver.find_element("css selector", "html")
        elem_html = elem.get_attribute("outerHTML")
        data = re.findall(r'window\.__SEARCH_RESULT__ = (.*?)</script>', elem_html)
        analysis_data.analysis(datalist, eval(data[0]))

def main():
    get_datalist()
    ope_xls.into_xls(datalist, "jobs.xls")
    ope_sqlite.into_sqlite(datalist, "jobs.db")
    driver.quit()


if __name__ == "__main__":
    main()