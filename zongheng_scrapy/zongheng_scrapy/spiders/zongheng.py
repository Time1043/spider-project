import scrapy

from zongheng_scrapy.items import ZonghengItem


class ZonghengSpider(scrapy.Spider):
    name = "zongheng"
    allowed_domains = ["book.zongheng.com"]
    start_urls = [f"https://book.zongheng.com/store/c0/c0/b0/u0/p{i}/v9/s9/t0/u0/i1/ALL.html"
                  for i in range(1, 20)]

    def parse(self, response):
        """解析列表页"""
        for item in response.xpath("//div[@class='store_collist']/div[not(@class='dotline')]"):
            zongheng_item = ZonghengItem()
            zongheng_item['novel_Name'] = item.xpath(".//div[@class='bookname']/a/text()").get()
            zongheng_item['novel_Author'] = item.xpath(".//div[@class='bookilnk']/a[1]/text()").get()
            zongheng_item['novel_Type'] = item.xpath(".//div[@class='bookilnk']/a[2]/text()").get()
            zongheng_item['novel_State'] = item.xpath(".//div[@class='bookilnk']/span[1]/text()").get()
            # zongheng_item['novel_Lastupdate'] = item.xpath(".//div[@class='bookilnk']/span[2]/text()").get()
            zongheng_item['novel_Latestchapters'] = item.xpath(
                ".//div[@class='bookupdate']/a[@class='fl']/text()").get()
            zongheng_item['novel_Synopsis'] = item.xpath(".//div[@class='bookintro']/text()").get()
            # yield zongheng_item

            url_detail = item.xpath(".//div[@class='bookname']/a/@href").get()
            print(zongheng_item['novel_Name'], url_detail)
            yield scrapy.Request(url=url_detail, callback=self.parse_detail, meta={"item": zongheng_item})

    def parse_detail(self, response):
        """解析详情页"""
        zongheng_item = response.meta["item"]
        print("------------------------------")
        print(response.text)
        click = response.xpath("//div[@class='book-info--nums']/div[1]/span/text()").get()
        recommend_all = response.xpath("//div[@class='book-info--nums']/div[2]/span/text()").get()
        recommend_week = response.xpath("//div[@class='book-info--nums']/div[3]/span/text()").get()
        word_count = response.xpath("//div[@class='book-info--nums']/div[4]/span/text()").get()
        time = response.xpath("//div[@class='book-info--chapter']/div/span/text()").get()

        if click is None:
            click = response.xpath("//div[@class='bookcount-numbox'][1]/span/text()").get()
            recommend_all = response.xpath("//div[@class='bookcount-numbox'][2]/span/text()").get()
            recommend_week = response.xpath("//div[@class='bookcount-numbox'][3]/span/text()").get()
            word_count = response.xpath("//span[@class='book-wordnum-num']/text()").get()
            time = response.xpath("//div[@class='bookup-lnk'][2]/text()").get()

        zongheng_item['click'] = click
        zongheng_item['recommend_all'] = recommend_all
        zongheng_item['recommend_week'] = recommend_week
        zongheng_item['word_count'] = word_count
        zongheng_item['novel_Lastupdate'] = time

        yield zongheng_item

        print(zongheng_item['novel_Name'])
        print({"click": click, "recommend_all": recommend_all, "recommend_week": recommend_week,
               "word_count": word_count, "time": time})
