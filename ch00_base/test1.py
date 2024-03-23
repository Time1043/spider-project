import hashlib
import json
from urllib.parse import quote

def js():
    """js逆向"""
    # 定义一个变量，它的值需要与第一次计算时的值相同
    offset_value = "%7B%22offset%22%3A%20%22%22%7D"

    # 使用json.dumps和quote来生成与第一次相同的字符串
    pagination_str_key_str = json.dumps({"offset": offset_value})
    pagination_str_key_url_encoded = quote(pagination_str_key_str)

    # 打印出来检查是否与第一次相同
    print(pagination_str_key_url_encoded)  # 应输出与第一次相同的URL编码后的字符串

    # 构建最终用于MD5计算的字符串
    en = [
        'mode=3',
        'oid=1651885800',
        f'pagination_str={pagination_str_key_url_encoded}',
        'plat=1',
        'seek_rpid=',
        'type=1',
        'web_location=1315875',
        'wts=1711116908',
    ]

    wt = "ea1db124af3c7062474693fa704f4ff8"
    jt = "&".join(en)
    st = jt + wt

    # 计算MD5哈希值
    MD5 = hashlib.md5()
    MD5.update(st.encode('utf-8'))
    w_rid = MD5.hexdigest()

    return w_rid

# 运行函数并打印结果
print(js())  # 应该输出 bb2597910d26c1a1ac1c8fd6564889a5