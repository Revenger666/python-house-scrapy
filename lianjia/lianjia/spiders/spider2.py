import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse
from lianjia.items import secondhanditem
class secondhandspider(scrapy.spiders.Spider):
    name = "lianjia2"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = []
    for page in range(3, 8):
        url1 = 'https://bj.lianjia.com/ershoufang/pg{}/'.format(page)
        start_urls.append(url1)

    custom_settings = {
        'ITEM_PIPELINES': {'lianjia.pipelines.secondhandline': 300},
    }

    def parse(self, response):

        item = secondhanditem()
        div_list = response.xpath("//*[@id=\"content\"]/div[1]/ul/li")

        #print(div_list)
        for each in div_list:
            item['name'] = each.xpath("./div[@class=\"info clear\"]/div[@class=\"flood\"]/div/a[1]/text()").extract_first()
            item['position'] = each.xpath("./div[@class=\"info clear\"]/div[@class=\"flood\"]/div/a[2]/text()").extract_first()
            item['types'] = each.xpath("./div[@class=\"info clear\"]/div[@class=\"address\"]/div/text()").extract_first()
            item['unitPrice'] = each.xpath("./div[@class=\"info clear\"]/div[@class=\"priceInfo\"]/div[2]/span/text()").extract_first()
            item['totalPrice'] = each.xpath("./div[@class=\"info clear\"]/div[@class=\"priceInfo\"]/div[1]/span/text()").extract_first()
            yield item
