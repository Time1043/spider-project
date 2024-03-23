# -*- coding: utf-8 -*-
# @Time    : 2024/3/22 20:15
# @Author  : yingzhu
# @FileName: test_q.py

import json
from urllib.parse import quote
import hashlib
import time

print(int(time.time()))


def js_param():
    """js逆向"""
    pagination_str_key = {"offset": ""}
    pagination_str_key_str = json.dumps(pagination_str_key)
    pagination_str_key_url = quote(pagination_str_key_str)
    print(pagination_str_key_url)  # %7B%22offset%22%3A%20%22%22%7D



    en = [
        'mode=3',
        'oid=1651885800',
        'pagination_str=%s' % pagination_str_key_url,
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


print(js_param())  # a947e9160aa37695cc1a4384e4fc3626
