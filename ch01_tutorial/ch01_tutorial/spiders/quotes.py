import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response, **kwargs):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                "text": quote.xpath("./span[@class='text']/text()").get(),
                "author": quote.xpath(".//small[@class='author']/text()").get(),
                "tags": quote.xpath("./div[@class='tags']/a[@class='tag']/text()").getall(),
            }
