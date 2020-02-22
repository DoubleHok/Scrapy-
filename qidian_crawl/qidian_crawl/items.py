# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianCrawlItem(scrapy.Item):
    # define the fields dfor your item here like:
    title = scrapy.Field()
    intro = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()


