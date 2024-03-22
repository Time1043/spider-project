from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response, **kwargs):  # 回调
        page = response.url.split("/")[-2]
        filename = f"res/quotes-{page}.html"
        Path(filename).write_bytes(response.body)
