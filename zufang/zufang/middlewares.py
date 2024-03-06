from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse

# 只需要修改下载器中间件，爬虫中间件不用管


class ZufangDownloaderMiddleware:
    # 当下载器中间件开始工作时，自动打开一个浏览器

    def __init__(self):
        self.driver = webdriver.Chrome()

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        # 下面这一行需要手动添加，作用是调用关闭浏览器的函数
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    # 每当爬虫文件向目标网址发送一次请求都会调用这个函数，用处就是返回该网址的源码

    def process_request(self, request, spider):
        self.driver.get(request.url) # 使用浏览器打开请求的URL
        body = self.driver.page_source # 获取网页HTML源码
        return HtmlResponse(url=self.driver.current_url, body=body, encoding='utf-8', request=request)

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

        # 该函数需要手动添加，作用是关闭浏览器

    def spider_closed(self, spider):
        self.driver.close()
        spider.logger.info("Spider closed: %s" % spider.name)
