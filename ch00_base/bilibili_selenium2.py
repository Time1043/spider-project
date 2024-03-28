# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/3/28 16:48
# @File    ：bilibili_selenium2.py
# @Function:
import csv
import json
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 网络请求
req_url = "https://www.bilibili.com/video/BV1Vj421o7NN/?spm_id_from=333.999.0.0&vd_source=c5bd4b1fb40a0cf2a6d098df40e54fa2"
cookie_file_path = "crawl/bilibili_cookie.txt"
# 持久化数据
csv_file = "crawl/bilibili_comments1.csv"
data_list = []


def get_cookie(wd):
    """登录获取并保存cookie 执行一遍就好"""
    wd.get("https://www.bilibili.com")
    wd.delete_all_cookies()
    time.sleep(20)  # 登录

    cookie_my = wd.get_cookies()
    cookie_jsons = json.dumps(cookie_my)
    with open(cookie_file_path, 'w') as f:
        f.write(cookie_jsons)

    wd.quit()


def login_in(wd):
    """读取上面保存的cookie 登录并加载视频页面"""
    wd.get(req_url)
    f = open(cookie_file_path, 'r')
    cookie = json.loads(f.read())
    for i in cookie:
        wd.add_cookie(i)

    wd.refresh()
    time.sleep(10)  # 让网页加载完毕 防止后面元素找不到


def parse_data_sub_list(reply_list,
                        attr_reply="reply-content", attr_username="sub-user-name",
                        attr_time="sub-reply-time", attr_like="sub-reply-like"):
    """根据attr 拿reply_list里的数据内容"""
    for i in reply_list:
        reply_type = "sub"
        sub_reply_username = i.find_element(By.CLASS_NAME, attr_username).text
        sub_reply_time = i.find_element(By.CLASS_NAME, attr_time).text
        sub_reply_like = i.find_element(By.CLASS_NAME, attr_like).text
        sub_reply_text = i.find_element(By.CLASS_NAME, attr_reply).text

        data_list.append([sub_reply_username, sub_reply_time, sub_reply_like, sub_reply_text, reply_type])


def parse_data_item_root(reply_item):
    """五个字段"""
    reply_type = "root"
    username = reply_item.find_element(By.CSS_SELECTOR, 'div[class="user-name"]').text
    reply_time = reply_item.find_element(By.CSS_SELECTOR, 'span[class="reply-time"]').text
    reply_like = reply_item.find_element(By.CSS_SELECTOR, 'span[class="reply-like"]').text
    root_reply_text = reply_item.find_element(By.CSS_SELECTOR, 'span[class="reply-content"]').text

    data_list.append([username, reply_time, reply_like, root_reply_text, reply_type])


def parse_data(reply_item):
    """解析html页面的数据"""
    # 根评论
    parse_data_item_root(reply_item)

    # 子评论
    view_more = reply_item.find_elements(By.CLASS_NAME, 'view-more-btn')
    if len(view_more) == 0:
        # 子评论无查看更多 直接获取内容
        sub_reply_list = reply_item.find_elements(By.CLASS_NAME, 'sub-reply-item')
        parse_data_sub_list(sub_reply_list)
    elif len(view_more) != 0:
        # 子评论查看更多
        wd.execute_script("arguments[0].click();", view_more[0])
        time.sleep(3)  # 等待3秒页面更新
        sub_reply_list = reply_item.find_elements(By.CLASS_NAME, 'sub-reply-item')
        parse_data_sub_list(sub_reply_list)

        # while True:
        #     pagination_btn = reply_item.find_elements(By.CLASS_NAME, 'pagination-btn')
        #     if len(pagination_btn) == 0:
        #         break  # 如果这条评论没有下一页子评论，则结束循环，获取完主评论后跳到下一条评论
        #     elif len(pagination_btn) != 0:
        #         # 如果有下一页，则点击下一页
        #         # 这里会有3种情况，分别是“只有下一页”、“上一页+下一页”、“只有上一页”
        #
        #         if len(pagination_btn) == 1 and pagination_btn[0].text == "上一页":
        #             break  # 针对只有上一页，则退出循环
        #         time.sleep(3)  # 等待网页加载
        #
        #         if len(pagination_btn) == 1 and pagination_btn[0].text == "下一页":
        #             # 针对只有下一页，则点击第一个按钮，即下一页
        #             wd.execute_script("arguments[0].click();", pagination_btn[0])
        #             time.sleep(3)  # 等待网页加载
        #             sub_reply_list = reply_item.find_elements(By.CLASS_NAME, 'sub-reply-item')  # 找到这一页完整的子评论
        #             parse_data_sub_list(sub_reply_list)
        #
        #         if len(pagination_btn) == 2:
        #             # 针对有上一页和下一页，我们要点击第二个按钮，也就是下一页
        #             wd.execute_script("arguments[0].click();", pagination_btn[1])
        #             time.sleep(3)  # 等待网页加载
        #             sub_reply_list = reply_item.find_elements(By.CLASS_NAME, 'sub-reply-item')  # 找到这一页完整的子评论
        #             parse_data_sub_list(sub_reply_list)
        #
        #         save_data()

        save_data()


def create_csv_if_not_exists(csv_file):
    """ 检查 CSV 文件是否存在，如果不存在则创建并添加表头 """
    os.makedirs(os.path.dirname(csv_file), exist_ok=True)
    if not os.path.isfile(csv_file):  # 如果文件不存在
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Username', 'Reply Time', 'Likes', 'Reply Content', 'Type'])
        print(f'Created {csv_file} and header written.')
    else:
        print(f'{csv_file} already exists.')


def append_to_csv(data_list, csv_file):
    """ 将信息追加到已存在的 CSV 文件 """
    with open(csv_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data_list)
    print(f'Data appended to {csv_file}')


def save_data():
    append_to_csv(data_list, csv_file)
    data_list.clear()  # 保存后要置空


def get_comments(wd):
    """主函数：获取已加载的所有评论函数"""
    login_in(wd)  # 登录

    # 加载当前页面出现了的所有评论
    comment_area = wd.find_element(By.CSS_SELECTOR, '#comment > div > div > div > div.reply-warp > div.reply-list')
    reply_item_list = comment_area.find_elements(By.CLASS_NAME, 'reply-item')  # 获得了当前加载的评论不是所有评论 动态加载

    # 动态加载 死循环
    while True:
        for reply_item in reply_item_list:
            parse_data(reply_item)

        # 当前加载的评论全部获取完毕，需要滑动页面，并获得新加载的评论
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        reply_item_list = comment_area.find_elements(By.CLASS_NAME, 'reply-item')


if __name__ == '__main__':
    print("------------------ start ------------------")

    create_csv_if_not_exists(csv_file)

    wd = webdriver.Chrome()
    # get_cookie(wd)
    get_comments(wd)

    print("------------------ end ------------------")
