# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tasks.models import Task

class PbotPipeline(object):
    def process_item(self, item, spider):
        return item

class djangoPipeline(object):
    def process_item(self, item, spider):
    	# item['task'] = Task.objects.get(id=3)
        item.save()
        return item