# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class DangdangDataPipeline(object):
    # def __init__(self):
    #     self.filename = open("DANGDANGdata.txt", "wb+")



    def process_item(self, item, spider):
        # jsontext = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # self.filename.write(jsontext.encode("utf-8"))
        base_dir=os.getcwd()
        filename=base_dir + '/DANGDANGdata.txt'
        with open(filename,'a') as f:
            f.write(item['title'] + '/')
            f.write(item['comment'] + '\n')
        return item


    # def close_spider(self, spider):
    #     self.filename.close()

