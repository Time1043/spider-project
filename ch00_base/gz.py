# -*- coding: utf-8 -*-
# @Time    : 2024/3/31 8:46
# @Author  : yingzhu
# @FileName: gz.py

import json
import re
import time

import requests
from bs4 import BeautifulSoup

json_file_path = 'help/free_changnan_url.json'
file_name = 'crawl/changnan.txt'


def req_gz_free():
    """爬取指定url的文章 抓包分析"""
    url = "https://mp.weixin.qq.com/s"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309092b) XWEB/9079 Flue',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cache-control': 'max-age=0',
        'x-wechat-key': '7ac31fc11733e01d2e99e38980d687291a52150e8da78e0697f16e5e5c7c9f592148b4a039fa842b0f088971d6d0250167bb99d52440f40e0ab4e142ffcf2723dc8e8ac30cbf196dcd19a67972ec851ef54b637e1944b2fd0ee8b6dc209806afaf6d54c02ada36eda5bc428ac6f0d1016c74923c37e34aea045b98a3077b5aef',
        'x-wechat-uin': 'MzEzNjEzNzc1Ng%3D%3D',
        'exportkey': 'n_ChQIAhIQle4ypdFFq%2FQ2Vc8anb8e2hLgAQIE97dBBAEAAAAAADWCNo8vF0wAAAAOpnltbLcz9gKNyK89dVj0K3AGERusLseH1iBfU4IJzdrVz8226on%2BeySDZZGlCfgAqH8cTchGeQuArnaZIrPjGrsCVm2JOuYijS0vuN%2F9naHBKLDoo6MBTeaVIFHoDzlx97HPlws2yneBs2ev6HeTdnEy9%2F8cXItmV%2BBjz%2B5POMKX1fIiaSHJXX8Yjy0S2FPLv5FmNNL0V%2BwSyB2%2BFkrH2CBWb8FiaTbS5uUb0Q7nqZC3lMiYdtjx2X%2B6fJUSqFjuVTsf%2Fa41YTEE',
        'upgrade-insecure-requests': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
    params = {
        "__biz": "MzA5NzI1ODkzNQ==",
        "mid": "2451450218",
        "idx": "1",
        "sn": "e5c06e14960e943742f2a0d07fe327b8",
        "chksm": "86d210a4cd5e203bfeac7014673c50b35c043e8d09b4a5e5cb75ec68ac4eb691807f14f1d774",
        "scene": "126",
        "sessionid": "1711847075",
        "subscene": "227",
        "clicktime": "1711847138",
        "enterid": "1711847138",
        "key": "7ac31fc11733e01d2e99e38980d687291a52150e8da78e0697f16e5e5c7c9f592148b4a039fa842b0f088971d6d0250167bb99d52440f40e0ab4e142ffcf2723dc8e8ac30cbf196dcd19a67972ec851ef54b637e1944b2fd0ee8b6dc209806afaf6d54c02ada36eda5bc428ac6f0d1016c74923c37e34aea045b98a3077b5aef",
        "ascene": "0",
        "uin": "MzEzNjEzNzc1Ng==",
        "devicetype": "Windows 11 x64",
        "version": "6309092b",
        "lang": "zh_CN",
        "countrycode": "CN",
        "exportkey": "n_ChQIAhIQle4ypdFFq/Q2Vc8anb8e2hLgAQIE97dBBAEAAAAAADWCNo8vF0wAAAAOpnltbLcz9gKNyK89dVj0K3AGERusLseH1iBfU4IJzdrVz8226on+eySDZZGlCfgAqH8cTchGeQuArnaZIrPjGrsCVm2JOuYijS0vuN/9naHBKLDoo6MBTeaVIFHoDzlx97HPlws2yneBs2ev6HeTdnEy9/8cXItmV+Bjz+5POMKX1fIiaSHJXX8Yjy0S2FPLv5FmNNL0V+wSyB2+FkrH2CBWb8FiaTbS5uUb0Q7nqZC3lMiYdtjx2X+6fJUSqFjuVTsf/a41YTEE",
        "acctmode": "0",
        "pass_ticket": "np4ckNMKro5lryfLhSuw6h4YS/AhvXKb61q+NkH7w+WOXLXnXujMi/TMhIV4N3C7q7GS2juoRHfxDe3etPIJDg==",
        "wx_header": "1",
        "fasttmpl_type": "0",
        "fasttmpl_fullversion": "7139752-zh_CN-zip",
        "fasttmpl_flag": "1",
    }
    resp = requests.get(url=url, headers=headers, params=params)
    resp_html = resp.text

    parse_html(resp_html)


def req_gz_free2():
    """爬取指定url的文章 简单爬取"""
    url = "https://mp.weixin.qq.com/s/HAI1TeKyR4jhiwv8FQbccQ"
    resp = requests.get(url=url)
    resp_html = resp.text

    parse_html(resp_html)


def req_gz_free3():
    """爬取指定url的文章 手动打螺丝"""

    article_url_list = []
    article_title_list = []
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for article in data["article_list"]:
            article_url_list.append(article.get("url", ""))
            article_title_list.append(article.get("title", ""))
    print(article_url_list)
    print(article_title_list)

    for i in range(len(article_url_list)):
        url = article_url_list[i]
        title = article_title_list[i]

        print("================================")
        resp = requests.get(url=url)
        resp_html = resp.text
        parse_html(resp_html, title)

        time.sleep(2)


def parse_html(resp_html, title):
    """从html中解析出文章内容"""
    soup_div = BeautifulSoup(resp_html, 'html.parser')
    target_div = soup_div.select_one('.rich_media_content')

    page_content_list = [title, ]
    print(title)
    for div in target_div:
        text_content = div.get_text(strip=True)
        text_content_clean = text_content.replace("&nbsp;", " ")
        page_content_list.append(text_content_clean)
    page_content_list_clean = [content for content in page_content_list if content]

    save_data(file_name, page_content_list_clean)


def save_data(file_name, data_list):
    """保存数据到文件"""
    with open(file_name, 'a', encoding='utf-8') as file:
        for item in data_list:
            file.write(item + '\n')
        file.write('\n' * 5)


if __name__ == '__main__':
    print("------------------ start ------------------")

    # req_gz_free()
    # req_gz_free2()
    req_gz_free3()

    print("------------------ end ------------------")
