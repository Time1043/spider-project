import scrapy


class BaidusearchSpider(scrapy.Spider):
    name = "baidusearch"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://baidu.com"]

    def parse(self, response):
        print(response.text)
