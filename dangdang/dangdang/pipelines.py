# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        # for i in range(1):
        for i in range(len(item["title"])):
            print("******")
            print(item["title"][i])
            print(item["link"][i])
            print(item["comment"][i])
        return item
