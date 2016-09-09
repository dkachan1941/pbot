# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# from scrapy.contrib_exp.djangoitem import DjangoItem
# from pmon.tasks.models import Article
 
# class Article_item(DjangoItem):
#     django_model = Poll


class PbotItem(scrapy.Item):
    price = scrapy.Field()
    name = scrapy.Field()
    unit = scrapy.Field()
    photo = scrapy.Field()