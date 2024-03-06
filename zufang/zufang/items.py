# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class zufangitem(scrapy.Item):
    title = scrapy.Field() # 标题
    price = scrapy.Field() #月租金
    position0 = scrapy.Field() #地址1
    position1 = scrapy.Field() #地址2
    position2 = scrapy.Field() #地址3
    information = scrapy.Field() #其他信息

