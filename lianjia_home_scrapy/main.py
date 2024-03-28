# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/3/21 16:38
# @File    ：main.py
# @Function:

from scrapy import cmdline

if __name__ == '__main__':
    print("--------------- start ---------------")
    cmdline.execute("scrapy crawl lianjia -O crawl/res.csv".split())
    print("--------------- end ---------------")
