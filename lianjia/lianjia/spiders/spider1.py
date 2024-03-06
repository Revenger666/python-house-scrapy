import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse
from lianjia.items import firsthanditem
class firsthandspider(scrapy.spiders.Spider):
    name = "lianjia1"
    allowed_domains = ["bj.fang.lianjia.com"]
    start_urls = []
    for page in range(3, 8):
        url1 = 'https://bj.fang.lianjia.com/loupan/pg{}/'.format(page)
        start_urls.append(url1)
    #for page in range(3, 8):
    #    url1 = 'https://bj.lianjia.com/ershoufang/pg{}/'.format(page)
    #    start_urls.append(url1)

    custom_settings = {
        'ITEM_PIPELINES': {'lianjia.pipelines.firsthandline': 300},
    }

    def parse(self, response):

        item = firsthanditem()
        div_list = response.xpath("/html/body/div[3]/ul[2]/li")
        #div_list = response.xpath("//*")
        #print(div_list)
        for each in div_list:

            item['name'] = each.xpath("./div[@class=\"resblock-desc-wrapper\"]/div[@class=\"resblock-name\"]/a/text()").extract_first()
            item['types'] = each.xpath("./div[@class=\"resblock-desc-wrapper\"]/div[@class=\"resblock-name\"]/span[@class=\"resblock-type\"]/text()").extract_first()
            item['position'] = each.xpath("./div[@class=\"resblock-desc-wrapper\"]/div[@class=\"resblock-location\"]/a/text()").extract_first()
            item['position1'] = each.xpath("./div[@class=\"resblock-desc-wrapper\"]/div[@class=\"resblock-location\"]/span[1]/text()").extract_first()
            item['position2'] = each.xpath("./div[@class=\"resblock-desc-wrapper\"]/div[@class=\"resblock-location\"]/span[2]/text()").extract_first()
            item['houseType'] = each.xpath("./div[@class=\"resblock-desc-wrapper\"]/a[@class=\"resblock-room\"]/span/text()").extract_first()
            item['space'] = each.xpath("./div[@class=\"resblock-desc-wrapper\"]/div[@class=\"resblock-area\"]/span/text()").extract_first()
            item['unitPrice'] = each.xpath("./div[@class=\"resblock-desc-wrapper\"]/div[@class=\"resblock-price\"]/div[@class=\"main-price\"]/span[@class = \"number\"]/text()").extract_first()
            item['totalPrice'] = each.xpath("./div[@class=\"resblock-desc-wrapper\"]/div[@class=\"resblock-price\"]/div[@class=\"second\"]/text()").extract_first()
            yield item
