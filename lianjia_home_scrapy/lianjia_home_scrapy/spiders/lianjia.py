import scrapy

from lianjia_home_scrapy.items import LianjiaHomeScrapyItem


class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = ["https://bj.lianjia.com/ershoufang/"]

    def parse(self, response):
        """解析url，带上地区参数和页面参数"""
        url_region_page = self.start_urls[0]
        yield scrapy.Request(url=url_region_page, callback=self.parse_data)
        region = response.xpath("//div[@data-role='ershoufang']/div/a/@href").getall()
        print(len(region))  # 17
        for rg in region:
            url_region = self.start_urls[0] + rg.split("/")[-2]
            for pg in range(1, 21):
                url_region_page = url_region + "/" + str(pg)
                yield scrapy.Request(url=url_region_page, callback=self.parse_data)

    def parse_data(self, response):
        """解析列表页数据"""
        for li in response.xpath("//ul[@class='sellListContent']/li"):
            try:
                house_item = LianjiaHomeScrapyItem()
                detail_url = li.xpath(".//div[@class='title']/a[@target='_blank']/@href").get()
                print(f"detail_url: {detail_url}")

                house_item["title"] = li.xpath(".//div[@class='title']/a[@target='_blank']/text()").get()
                house_item["location"] = li.xpath(".//div[@class='positionInfo']/a[@target='_blank']/text()").getall()
                house_item["basic_attributes"] = li.xpath(".//div[@class='houseInfo']/text()").get()
                house_item["follow"] = li.xpath(".//div[@class='followInfo']/text()").get().split("/")[0]
                house_item["time_rl"] = li.xpath(".//div[@class='followInfo']/text()").get().split("/")[-1]
                house_item["label"] = li.xpath(".//div[@class='tag']/span/text()").getall()
                house_item["price"] = li.xpath(".//div[@class='priceInfo']/div[1]/span/text()").get()
                house_item["price_avg"] = li.xpath(".//div[@class='priceInfo']/div[2]/span/text()").get()

                yield house_item
            except Exception as e:
                print(e)

    #         if detail_url is not None:
    #             yield scrapy.Request(url=detail_url, callback=self.parse_more, meta={"house_item": house_item})
    #
    # def parse_more(self, response):
    #     """爬取详情页信息"""
    #     house_item = response.meta["house_item"]
    #     # 数据
    #     basic_attributes_list = response.xpath(
    #         ".//div[@class='base']/div[@class='content']/ul/li/text()").getall()
    #     transaction_attributes_list = response.xpath(
    #         ".//div[@class='transaction']/div[@class='content']/ul/li/span[2]/text()").getall()
    #     basic_attributes_list_clean = [item.strip() for item in basic_attributes_list if item.strip()]
    #     transaction_attributes_list_clean = []
    #
    #     print(basic_attributes_list_clean)
    #
    #     # 信息头
    #     basic_attributes_head = response.xpath(
    #         ".//div[@class='base']/div[@class='content']/ul/li/text()").getall()
    #     transaction_attributes_head = response.xpath(
    #         ".//div[@class='transaction']/div[@class='content']/ul/li/span[2]/text()").getall()
    #     basic_attributes_head_clean = []
    #     transaction_attributes_head_clean = []
    #     print(basic_attributes_head)
    #
    #
    #     for tr in transaction_attributes_list:
    #         tr.replace("\n", "").strip()
    #         transaction_attributes_list_clean.append(tr)
    #     for ba in basic_attributes_head:
    #         ba.replace("\n", "").strip()
    #         basic_attributes_head_clean.append(ba)
    #     for tr in transaction_attributes_head:
    #         tr.replace("\n", "").strip()
    #         transaction_attributes_head_clean.append(tr)
    #
    #     house_item["basic_attributes"] = dict(
    #         zip(basic_attributes_head_clean, basic_attributes_list_clean))
    #     house_item["transaction_attributes"] = dict(
    #         zip(transaction_attributes_head_clean, transaction_attributes_list_clean))
    #     print("--------------------------------------------------------")
    #     # print(house_item["basic_attributes"])
    #     # print(house_item["transaction_attributes"])
    #     yield house_item
