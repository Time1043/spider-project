import scrapy

from lotto_scrapy.items import LottoScrapyItem


class SsqSpider(scrapy.Spider):
    name = "ssq"
    allowed_domains = ["500.com"]
    start_urls = ["https://datachart.500.com/ssq/"]

    def parse(self, response, **kwargs):
        trs = response.xpath("//tbody[@id='tdata']/tr")
        for tr in trs:
            if tr.xpath("./@class").extract_first() == "tdbck": continue

            lotto_item = LottoScrapyItem()
            lotto_item["issue"] = tr.xpath("./td[@align='center']/text()").extract_first().strip()
            lotto_item["red_ball"] = tr.xpath("./td[@class='chartBall01']/text()").extract()
            lotto_item["blue_ball"] = tr.xpath("./td[@class='chartBall02']/text()").extract_first()

            yield lotto_item  # scrapy.item
