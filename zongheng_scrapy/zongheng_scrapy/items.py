# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZonghengScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ZonghengItem(scrapy.Item):
    novel_Name = scrapy.Field()
    novel_Author = scrapy.Field()
    novel_Type = scrapy.Field()
    novel_State = scrapy.Field()
    novel_Lastupdate = scrapy.Field()
    novel_Latestchapters = scrapy.Field()
    novel_Synopsis = scrapy.Field()
    click = scrapy.Field()
    recommend_all = scrapy.Field()
    recommend_week = scrapy.Field()
    word_count = scrapy.Field()
