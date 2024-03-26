import scrapy

from lianjia_home_scrapy.items import LianjiaHomeScrapyItem


class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = ["https://bj.lianjia.com/ershoufang/"]

    def parse(self, response):
        for li in response.xpath("//ul[@class='sellListContent']/li"):
            try:
                item = LianjiaHomeScrapyItem()
                item["title"] = li.xpath(".//div[@class='title']/a[@target='_blank']/text()").get()
                item["location"] = li.xpath(".//div[@class='positionInfo']/a[@target='_blank']/text()").getall()
                item["condition"] = li.xpath(".//div[@class='houseInfo']/text()").get()
                item["follow"] = li.xpath(".//div[@class='followInfo']/text()").get().split("/")[0]
                item["time"] = li.xpath(".//div[@class='followInfo']/text()").get().split("/")[-1]
                item["label"] = li.xpath(".//div[@class='tag']/span/text()").getall()
            except Exception as e:
                print(e)
            yield item
