# -*- coding: utf-8 -*-
from jinritoutiao.items import *
from jinritoutiao.DataSave import *
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JinritoutiaoPipeline(object):
	def __init__(self):	
		self.datalink = DataSave()

	def process_item(self, item, spider):
		if isinstance(item,wenda):
			self.datalink.add_wenda(item['new_id'],item['new_url'],item['new_title'],item['new_content'])
		else:
			self.datalink.add_article(item['new_id'],item['new_url'], item['new_title'],item['new_content'],item['new_from'], item['new_time'])
		return item