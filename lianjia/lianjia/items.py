# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class firsthanditem(scrapy.Item):
    name = scrapy.Field()
    position = scrapy.Field()
    position1 = scrapy.Field()
    position2 = scrapy.Field()
    types = scrapy.Field()
    houseType = scrapy.Field()
    space = scrapy.Field()
    unitPrice = scrapy.Field()
    totalPrice = scrapy.Field()

class secondhanditem(scrapy.Item):
    name = scrapy.Field()
    position = scrapy.Field()
    types = scrapy.Field()
    unitPrice = scrapy.Field()
    totalPrice = scrapy.Field()