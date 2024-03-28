# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaHomeScrapyItem(scrapy.Item):
    title = scrapy.Field()
    location = scrapy.Field()
    basic_attributes = scrapy.Field()
    transaction_attributes = scrapy.Field()
    follow = scrapy.Field()
    time_rl = scrapy.Field()
    time = scrapy.Field()
    label = scrapy.Field()
    price = scrapy.Field()
    price_avg = scrapy.Field()
