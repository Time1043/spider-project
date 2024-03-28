# -*- coding: utf-8 -*-
# @Time    : 2024/3/22 18:08
# @Author  : yingzhu
# @FileName: bilibili_api.py

import hashlib
import time
from datetime import datetime

import requests
import csv


def req_comment():
    """单个视频、单页的评论抓取"""
    timestamp = int(time.time())
    w_rid = js_param(timestamp)

    url = f"https://api.bilibili.com/x/v2/reply/wbi/main"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Referer': 'https://www.bilibili.com/video/BV1Vj421o7NN/?spm_id_from=333.880.my_history.page.click&vd_source=c5bd4b1fb40a0cf2a6d098df40e54fa2',
        'Cookie': "buvid3=08EB9CF5-7965-5F82-1C23-BC3A0B50772167420infoc; b_nut=1699952667; i-wanna-go-back=-1; b_ut=7; _uuid=5395B1BD-958C-EEFC-3E103-2AD182E41033B68688infoc; buvid_fp=0d3de04bafc6a6d97cadfe5d624c3bb3; enable_web_push=DISABLE; buvid4=5AD4DE82-A501-B690-E0B1-DAE11C66D2C669381-023111409-; CURRENT_FNVAL=4048; header_theme_version=CLOSE; DedeUserID=259090980; DedeUserID__ckMd5=17f29169a9316ab9; rpdid=|(u))Ykllu)~0J'u~||k|~k~); CURRENT_QUALITY=80; PVID=1; home_feed_column=5; SESSDATA=dc6a8e24%2C1719228414%2Cece6f%2Ac2CjCzleLJ9LiYnWS0ynP_s98hoVXjM8c5j3Y9iQVd5IVQy_U8fPB6n-_51asuEKgNxGMSVm9PMUJURG5Cd2ZQM083M1hCdllvZXFsVUprOUNqbVdReG1CU0VpaGdQVjhtVXFjcEl2enhockpGT0RQampCT3daR2NlUGlLVHBJc3A4MXFVRDZiVVRnIIEC; bili_jct=9436937119ec3769c880659181936cda; FEED_LIVE_VERSION=V8; browser_resolution=1598-882; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTEzNjE5NDQsImlhdCI6MTcxMTEwMjY4NCwicGx0IjotMX0.0FhgDDoSaD7oUfr-vekC6N_rN80KZxfk0u87JyDU7GQ; bili_ticket_expires=1711361884; b_lsid=397958A7_18E65EB9B3F; sid=7rt1p300; bp_video_offset_259090980=911707474024726533"
    }

    params = {
        'oid': '1651885800',
        'type': '1',
        'mode': '3',
        'pagination_str': '{"offset":""}',
        'plat': '1',
        'seek_rpid': '',
        'web_location': '1315875',
        'w_rid': "3f54248b2eb161205f9dd77ba4f52833",
        'wts': "1711111789",
    }
    print(w_rid, timestamp)

    resp = requests.get(url=url, headers=headers, params=params)
    # print(resp.json())
    session_id = parse_data(resp)

    # 翻页请求
    params2 = {
        'oid': '1651885800',
        'type': '1',
        'mode': '3',
        'pagination_str': '{"offset":"{"type":1,"direction":1,"session_id":"%s","data":{}}"}' % session_id,
        'plat': '1',
        'seek_rpid': '',
        'web_location': '1315875',
        'w_rid': "3f54248b2eb161205f9dd77ba4f52833",
        'wts': "1711111789",
    }


def parse_data(resp):
    session_id = resp.json()["data"]["cursor"]["session_id"]
    print(f"session_id: {session_id}")

    for item in resp.json()["data"]["replies"]:
        content = item["content"]["message"]
        like = item["like"]
        uname = item["member"]["uname"]
        sex = item["member"]["sex"]
        location = item["reply_control"]["location"].replace("IP属地：", "")

        reply_content_list = []
        replies = item["replies"]
        for reply in replies:
            reply_content = reply["content"]["message"]
            reply_content_list.append(reply_content)

        f = open("crawl/data.csv", mode="a", encoding="utf-8", newline='')
        (csv.DictWriter(f, fieldnames=["uname", "like", "content", "sex", "location", "reply_content_list"])
         .writerow({"uname": uname, "like": like, "content": content, "sex": sex, "location": location,
                    "reply_content_list": reply_content_list}))
        f.close()

    return session_id


def js_param(timestamp):
    """js逆向"""
    en = [
        'mode=3',
        'oid=1651885800',
        'pagination_str=%7B%22offset%22%3A%22%22%7D',
        'plat=1',
        'seek_rpid=',
        'type=1',
        'web_location=1315875',
        'wts=1711116908',
    ]

    wt = "ea1db124af3c7062474693fa704f4ff8"
    jt = "&".join(en)
    st = jt + wt
    MD5 = hashlib.md5()
    MD5.update(st.encode('utf-8'))
    w_rid = MD5.hexdigest()
    return w_rid


if __name__ == '__main__':
    print("------------------ start ------------------")

    req_comment()

    print("------------------ end ------------------")
