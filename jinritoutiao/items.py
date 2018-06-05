# -*- coding: utf-8 -*-
import _md5
import string
# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

sall = (string.ascii_letters+string.digits).encode('utf8')
sa = _md5.md5(sall)
sa

class news(scrapy.Item):
    # define the fields for your item here like:
    new_url = scrapy.Field()  # 新闻连接
    new_title = scrapy.Field()  # 新闻标题
    new_content = scrapy.Field()  # 新闻正文
    new_id = scrapy.Field()  # 新闻ID
    new_time = scrapy.Field()  # 新闻时间
    new_from = scrapy.Field()  # 新闻来源


class wenda(scrapy.Item):
    """docstring for wenda"""
    new_url = scrapy.Field()  # 新闻连接
    new_title = scrapy.Field()  # 新闻标题
    new_content = scrapy.Field()  # 新闻正文
    new_id = scrapy.Field()  # 新闻ID

class comment(scrapy.Item):
    com_content = scrapy.Field()  # 评论内容
    com_user_name = scrapy.Field()  # 评论者昵称
    com_user_id = scrapy.Field()  # 评论者ID
