# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from pbot.items import PbotItem, djangoArticle
from scrapy.contrib.linkextractors import LinkExtractor
import cssselect
from scrapy.shell import inspect_response
from bs4 import BeautifulSoup

def css_to_xpath(css):
    return cssselect.HTMLTranslator().css_to_xpath(css)

class BaucenterSpider(CrawlSpider):
    name = "baucenter"
    allowed_domains = ["https://www.baucenter.ru", "www.baucenter.ru", "https://baucenter.ru", "baucenter.ru"]
    start_urls = (
        'https://www.baucenter.ru/',
    )
    # handle_httpstatus_list = [404, 500]
    # custom_settings = {'DOWNLOAD_DELAY':1, 'ITEM_PIPELINES':['market.pipelines.ActionsXlsPipeline']}

    def __init__(self, *a, **kw):
        super(BaucenterSpider, self).__init__(*a, **kw)
        self.myargument = kw.get('id_task', '')

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths=(
                css_to_xpath('.top-nav_catalog a.top-nav_catalog_heading'),
                css_to_xpath('.categories_row_item'),
                # css_to_xpath('.categories_row_item'),
                # css_to_xpath('.categories_row_item'),
            )
        ), callback='parse_arts', follow=True),
    )

    def parse_arts(self, response):
        print("*"*100)
        
        items = response.selector.css('.catalog_item')
        # if len(items) > 0:
        	# inspect_response(response, self)
        for item in items:
        
            try:
                act_name_lst = item.css('.catalog_item_heading').extract()
                act_name = BeautifulSoup(' '.join(str(elem.encode('utf-8')) for elem in act_name_lst), "lxml").get_text().replace(" .", "").replace(" ", "").replace("\n", "").replace("\t", "").encode('utf-8')
            except Exception as e:
                act_name = False
                # self.loggger.error(str(e))
                
            try:
                price_lst = item.css('.price-block .price-block_price').extract() 
                act_price = BeautifulSoup(' '.join(str(elem.encode('utf-8')) for elem in price_lst), "lxml").get_text().replace(" .", "").replace(" .", "").replace(" ", "").replace("\n", "").replace("\t", "").encode('utf-8')
            except Exception as e:
                act_price = ""
                # self.loggger.error(str(e))
                
            try:
                act_image = item.css('.catalog_item_image').xpath('@src').extract()[0].replace("//", "").replace(" .", "").replace(" ", "").replace("\n", "").replace("\t", "").encode('utf-8')
            except Exception as e:
                act_image = ""
                # self.loggger.error(str(e))

            try:
                lst = item.css('.price-block_price_pack').extract()
                unit = BeautifulSoup(' '.join(str(elem.encode('utf-8')) for elem in lst), "lxml").get_text().replace(" .", "").replace(" ", "").replace("\n", "").replace("\t", "").encode('utf-8')
            except Exception as e:
                unit = ""
                # self.loggger.error(str(e))
                
            if act_name:
                print(act_name)
                print(act_price)
                print(act_image)
                return djangoArticle(name=act_name, price=act_price, photo_path=act_image, unit=unit, task = self.id_task, competitor="Бауцентр")
                # yield PbotItem(
                #     name = act_name,
                #     price = act_price,
                #     image = act_image,
                #     unit = unit,
                # )