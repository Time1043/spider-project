import scrapy


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    rank = scrapy.Field()
    label = scrapy.Field()
    area = scrapy.Field()
    time = scrapy.Field()
    duration = scrapy.Field()
    introduction = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    role = scrapy.Field()
