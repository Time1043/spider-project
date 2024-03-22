import scrapy


class LottoScrapyItem(scrapy.Item):
    issue = scrapy.Field()
    red_ball = scrapy.Field()
    blue_ball = scrapy.Field()
