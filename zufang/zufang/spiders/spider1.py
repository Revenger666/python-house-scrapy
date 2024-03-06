import scrapy

from zufang.items import zufangitem


class Zufangspider(scrapy.spiders.Spider):
    name = "xian" #  爬虫名字分别为 beijing shanghai  guangzhou  shenzhen  xian
    allowed_domains = ["xa.lianjia.com"] # 爬取的起始页面
    start_urls = []
    for page in range(1, 101):  # 共100页，所以利用一个循环来爬取
        url1 = 'https://xa.lianjia.com/zufang/pg{}/'.format(page)
        start_urls.append(url1)

    custom_settings = {
        'ITEM_PIPELINES': {'zufang.pipelines.zufangline': 300},
    }

    def parse(self, response, **kwargs):

        item = zufangitem()
        div_list = response.xpath("//*[@id=\"content\"]/div[1]/div[1]/div")

        #  通过XPATH来分析爬取到的内容，并提取需要的数据
        for each in div_list:
            item['title'] = each.xpath("normalize-space(./div/p[1]/a/text())").extract_first()
            item['price'] = each.xpath("normalize-space(./div/span/em/text())").extract_first()
            item['position0'] = each.xpath("./div/p[2]/a[1]/text()").extract_first()
            item['position1'] = each.xpath("./div/p[2]/a[2]/text()").extract_first()
            item['position2'] = each.xpath("./div/p[2]/a[3]/text()").extract_first()
            item['information'] = each.xpath("normalize-space(./div/p[2])").extract_first()
            yield item
