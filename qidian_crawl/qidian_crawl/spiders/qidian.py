# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qidian_crawl.items import QidianCrawlItem


class QidianSpider(CrawlSpider):
    name = 'qidian'  # 爬虫名称 启动爬虫时使用：scrapy crawl <爬虫名称>
    allowed_domains = ['qidian.com']  # 限定爬取范围
    '''
    爬虫的起始地址，期相应可食用 parse_start_url(response) 进行专门处理。
    '''

    start_urls = ['http://qidian.com/free/all?orderId=&vip=hidden&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=1&page=1']

    def start_requests(self):  # 启动时设置Cookies,Spider的特性
        cookies = 'e1=%7B%22pid%22%3A%22qd_P_free%22%2C%22eid%22%3A%22qd_B58%22%7D; e2=%7B%22pid%22%3A%22qd_P_limitfree%22%2C%22eid%22%3A%22qd_E01%22%2C%22l1%22%3A4%7D; _csrfToken=E5kaL3iBLXpM94JP4yoeUfhmV6euFNEweGd7uew0; newstatisticUUID=1566396538_1068486547; _qda_uuid=d54ae72a-9db9-6ad0-3502-fc367fbd3cac; e1=%7B%22pid%22%3A%22qd_P_limitfree%22%2C%22eid%22%3A%22qd_E01%22%2C%22l1%22%3A4%7D; e2=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%2C%22l1%22%3A3%7D'
        cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split(';')}
        yield scrapy.Request(self.start_urls[0], cookies=cookies)

    '''
    链接URL的提取和处理规则
    '''
    rules = (
        Rule(LinkExtractor(allow=r'book.qidian.com/info/\d+'), callback='parse_item', follow=False),
        Rule(LinkExtractor(
            allow=r'//www\.qidian\.com/free/all\?orderId=&vip=hidden&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=1&page=\d+'),
            follow=True),
    )

    def parse_item(self, response):  # 回调函数
        item = QidianCrawlItem()
        item['url'] = response.request._url
        item['title'] = response.xpath("//div[@class='book-info ']/h1/em/text()").extract_first()
        item['author'] = response.xpath("//div[@class='book-info ']/h1/span/a/text()").extract_first()
        item['intro'] = response.xpath("//div[@class='book-info ']//p[@class='intro']/text()").extract_first()
        yield item

