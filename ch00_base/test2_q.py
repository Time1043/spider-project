# -*- coding: utf-8 -*-
# @Time    : 2024/3/23 7:00
# @Author  : yingzhu
# @FileName: test2_q.py

import json
from urllib.parse import urlencode

pagination_params = {
  "offset": {
    "type": 1,
    "direction": 1,
    "session_id": "1752216768982478",
    "data": {}
  }
}

# 将字典转换为JSON字符串
pagination_str_json = json.dumps(pagination_params)

# 手动URL编码JSON字符串中的双引号和其他特殊字符
def url_encode_json(json_str):
    # 替换JSON中的双引号为URL编码的双引号
    encoded_str = json_str.replace('"', '\\"')
    # 将编码后的字符串用作URL参数
    return encoded_str

# 对JSON字符串进行URL编码
encoded_pagination_str = url_encode_json(pagination_str_json)

# 构建URL参数
url_params = urlencode({'pagination_str': encoded_pagination_str})

# 打印URL参数
print(url_params)

"""
result
%7B%22offset%22%3A%22%7B%5C%22type%5C%22%3A1%2C%5C%22direction%5C%22%3A1%2C%5C%22
session_id%5C%22%3A%5C%221752216768982478%5C%22%2C%5C%22data%5C%22%3A%7B%7D%7D%22%7D

run
%7B%22offset%22%3A%20%7B%22type%22%3A%201%2C%20%22direction%22%3A%201%2C%20%22
session_id%22%3A%20%221752216768982478%22%2C%20%22data%22%3A%20%7B%7D%7D%7D

run2 
%7B%5C%22offset%5C%22%3A+%7B%5C%22type%5C%22%3A+1%2C+%5C%22direction%5C%22%3A+1%2C+%5C%22
session_id%5C%22%3A+%5C%221752216768982478%5C%22%2C+%5C%22data%5C%22%3A+%7B%7D%7D%7D
"""