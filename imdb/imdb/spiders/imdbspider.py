# coding:utf-8

from scrapy.spiders import CrawlSpider, Request, Rule
from imdb.items import ImdbItem
from scrapy.linkextractors import LinkExtractor


class ImdbSpider(CrawlSpider):
    name = 'imdb'
    allowed_domains = ['www.imdb.cn']
    rules = (
        Rule(LinkExtractor(allow=r"/title/tt\d+$"), callback="parse_imdb", follow=True),
    )

    def start_requests(self):
        pages = []
        for i in range(1, 14616):
            url = "http://www.imdb.cn/nowplaying/" + str(i)
            yield Request(url=url, callback=self.parse)

    def parse_imdb(self, response):
        item = ImdbItem()
        item['url'] = response.url
        item['title'] = "".join(response.xpath('//*[@class="fk-3"]/div[@class="hdd"]/h3/text()').extract())
        pass
