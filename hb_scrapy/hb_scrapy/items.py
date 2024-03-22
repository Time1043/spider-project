import scrapy


class HbScrapyItem(scrapy.Item):
    tp_url = scrapy.Field()
    title = scrapy.Field()
