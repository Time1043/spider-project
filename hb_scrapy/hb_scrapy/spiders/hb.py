import re
from urllib.parse import quote

import scrapy
from scrapy import Request

from hb_scrapy.items import HbScrapyItem


class HbSpider(scrapy.Spider):
    name = "hb"
    allowed_domains = ["huaban.com"]
    start_urls = ["https://api.huaban.com/search/file"]

    def parse(self, response):
        """指定关键词、指定数量"""

        key_word = "春天"
        limit = "40"
        page = range(1, 16)

        for p in page:
            params = {
                "text": key_word,
                "sort": "all",
                "limit": limit,
                "page": p,
                "position": "search_pin",
                "fields": "pins:PIN, total, facets, split_words, relations, rec_topic_material",
            }
            url_with_params = response.urljoin('?' + '&'.join([f'{k}={v}' for k, v in params.items()]))
            yield scrapy.Request(url_with_params, callback=self.parse_json, meta={"key_word": key_word})

    def parse_json(self, response):
        """拿到详情页url，即url_detail，后将此url封装成Request对象给调度器"""

        key_word = response.meta["key_word"]
        count = 0
        for item in response.json()["pins"]:
            pin_id = item["pin_id"]
            title = f"{count}_{pin_id}_" + item.get("raw_text", "")
            title_clean = re.sub(r'[<>:"/\\|?*\s]', '_', title).strip()
            url_detail = f"https://huaban.com/pins/{pin_id}?searchWord={quote(key_word)}"
            count += 1
            print(title_clean, url_detail)
            yield Request(url=url_detail, callback=self.pares_url, meta={"title": title_clean})

    def pares_url(self, response, **kwargs):
        """在详情页html中由xpath解析到图片的url，后封装成Item给管道"""

        hb_item = HbScrapyItem()
        hb_item["title"] = response.meta["title"]
        hb_item["tp_url"] = response.xpath(
            "//div[@class='wrapper undefined']/div/div/div/div/div/div/div/img/@src").extract_first()
        print(hb_item["tp_url"])
        yield hb_item
