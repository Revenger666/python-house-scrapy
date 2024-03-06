from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from lianjia.spiders.spider1 import firsthandspider
from lianjia.spiders.spider2 import secondhandspider

configure_logging()
runner = CrawlerRunner()
runner.crawl(firsthandspider)
runner.crawl(secondhandspider)
d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run()
"""
from scrapy import cmdline

cmdline.execute("scrapy crawl spider1".split())
cmdline.execute("scrapy crawl spider2".split())

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

crawler = CrawlerProcess(settings)

crawler.crawl('spider1')
crawler.crawl('spider2')

crawler.start()"""