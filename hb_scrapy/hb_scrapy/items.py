import scrapy


class HbScrapyItem(scrapy.Item):
    title = scrapy.Field()
    tp_url = scrapy.Field()
    local_path = scrapy.Field()
