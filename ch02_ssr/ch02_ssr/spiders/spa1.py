import scrapy
from scrapy import Request

from ch02_ssr.items import MovieItem


class Spa1Spider(scrapy.Spider):
    name = "spa1"
    allowed_domains = ["spa1.scrape.center"]
    start_urls = [f"https://spa1.scrape.center/page/{i}" for i in range(1, 11)]

    def parse_detail(self, response):
        movie_item = response.meta["movie_item"]

        movie_item["introduction"] = response.xpath("//div[@class='drama']/p/text()").get().strip()
        movie_item["director"] = response.xpath("//p[@class='name text-center m-b-none m-t-xs']/text()").get()
        movie_item["actor"] = response.xpath(
            "//p[@class='el-tooltip name text-center m-b-none m-t-xs item']/text()").getall()
        movie_item["role"] = response.xpath(
            "//p[@class='el-tooltip role text-center m-b-none m-t-xs item']/text()").getall()

        yield movie_item  # 最终返回

    def parse(self, response):
        for item in response.xpath("//div[@class='el-card item m-t is-hover-shadow']"):
            movie_item = MovieItem()
            movie_item["title"] = item.xpath(".//h2[@class='m-b-sm']/text()").get()
            movie_item["rank"] = item.xpath(".//p[@class='score m-t-md m-b-n-sm']/text()").get().strip()
            movie_item["label"] = item.xpath(".//div[@class='categories']/button/span/text()").getall()
            movie_item["area"] = item.xpath(".//div[@class='m-v-sm info']/span[1]/text()").get()
            movie_item["time"] = item.xpath(".//div[@class='m-v-sm info']/span[3]/text()").get()
            movie_item["duration"] = item.xpath(".//div[@class='m-v-sm info'][2]/span/text()").get()

            # 详情页
            detail_utl = "https://spa1.scrape.center" + item.xpath(".//div[@class='el-row']/div/a/@href").get()
            yield Request(detail_utl, callback=self.parse_detail, meta={"movie_item": movie_item})  # 前面数据传递
