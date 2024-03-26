# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaHomeScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    location = scrapy.Field()
    condition = scrapy.Field()
    follow = scrapy.Field()
    time = scrapy.Field()
    label = scrapy.Field()

