# -*- coding: utf-8 -*-
# @Time    : 2024/3/22 15:55
# @Author  : yingzhu
# @FileName: hb.py

import os
import re

import requests
from lxml import etree


def req_tp():
    url = "https://api.huaban.com/search/file?text=%E9%A3%8E%E6%99%AF&sort=all&limit=40&page=1&position=search_pin&fields=pins:PIN,total,facets,split_words,relations,rec_topic_material"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    resp = requests.get(url=url, headers=headers)

    count = 0
    for item in resp.json()["pins"]:
        pin_id = item["pin_id"]
        title = f"{count}_" + item.get("raw_text", "")
        title_cleaned = re.sub(r'[<>:"/\\|?*]', '_', title).strip()
        url2 = f"https://huaban.com/pins/{pin_id}?searchWord=%E9%A3%8E%E6%99%AF"  # 详情页url
        count += 1

        req_html_url(url2, title_cleaned)


def req_html_url(url, title):
    resp = requests.get(url)
    item_url = etree.HTML(resp.text).xpath('//*[@id="pin_detail"]/div[1]/div[1]/div/div/img/@src')[0]  # 图片url
    resp_tp = requests.get(url=item_url)

    folder_path = "./crawl"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(f'{folder_path}/{title}.jpg', 'wb') as f:
        f.write(resp_tp.content)


if __name__ == '__main__':
    print("------------------ start ------------------")

    req_tp()

    print("------------------ end ------------------")
