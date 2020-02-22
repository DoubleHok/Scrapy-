# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from qidian_crawl.items import QidianCrawlItem
import json


class QidianCrawlPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, QidianCrawlItem):  # 仅处理QidainCrawItem, 其他Item不予处理
            # 将文章数据保存到文件
            with open('qidain.txt', 'a', encoding='utf-8') as f:
                json.dump(dict(item), f, ensure_ascii=False, indent=2)
        return item

