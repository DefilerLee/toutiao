# -*- coding: utf-8 -*-
import scrapy
import json
import re
from jinritoutiao.get_url import get_url
from jinritoutiao.items import *

class IndexSpider(scrapy.Spider):

    name = 'index'
    allowed_domains = ['www.toutiao.com']
    start_urls = [  # 'http://www.toutiao.com/',  # 推荐
        # 'https://www.toutiao.com/ch/news_hot/',  # 热点
        # 'https://www.toutiao.com/ch/news_image/',  # 图片
        # 'https://www.toutiao.com/ch/news_tech/',  # 科技
        # 'https://www.toutiao.com/ch/news_entertainment/',  # 娱乐
        # 'https://www.toutiao.com/ch/news_game/',  # 游戏
        # 'https://www.toutiao.com/ch/news_sports/',  # 体育
        # 'https://www.toutiao.com/ch/news_car/',  # 汽车
        # 'https://www.toutiao.com/ch/news_finance/'  # 财经
        # 'https://www.toutiao.com/ch/funny/',  # 搞笑
        # 'https://www.toutiao.com/ch/news_military/',  # 军事
        # 'https://www.toutiao.com/ch/news_world/',  # 国际
        # 'https://www.toutiao.com/ch/news_fashion/',  # 时尚
        # 'https://www.toutiao.com/ch/news_travel/',  # 旅游
        # 'https://www.toutiao.com/ch/news_discovery/',  # 探索
        # 'https://www.toutiao.com/ch/news_baby/',  # 育儿
        # 'https://www.toutiao.com/ch/news_regimen/',  # 养生
        # 'https://www.toutiao.com/ch/news_essay/',  # 美文
        # 'https://www.toutiao.com/ch/news_history/',  # 历史
        'https://www.toutiao.com/ch/news_food/',  # 美食
    ]

    def __init__(self):
        super(IndexSpider, self).__init__()

    def start_requests(self):
        headers = {}
        for url in self.start_urls:
            geturl = get_url()
            geturl.open_url(url)
            yield self.get_request(geturl)

    def get_request(self,geturl,max_behot_time='0',ua=False):
        """
        返回接口请求

        """
        headers={}
        user_agent = geturl.get_user_agent()
        cookie = geturl.get_cookie()
        url = geturl.get_url(str(max_behot_time))
        meta = {
            'get_url':geturl,
            'ua':ua
        }
        headers['User-Agent'] = user_agent
        return scrapy.Request(url,cookies=cookie,headers=headers,meta=meta)

    def parse(self, response):
        """
        解析JSON

        """
        text = response.text
        res = json.loads(text)
        if res['message'] == 'success':
            for x in res['data']:
                art_id = x['item_id']
                url = 'https://www.toutiao.com/a'+art_id+'/'
                if x['article_genre'] == 'wenda':
                    yield scrapy.Request(url,callback=self.parse_wenda,meta={'js':x,'url':url})
                else:
                    yield scrapy.Request(url,callback=self.parse_article,meta={'js':x,'url':url})
            max_behot_time = res['next']['max_behot_time']
            geturl = response.meta['get_url']
            yield self.get_request(geturl,max_behot_time=max_behot_time,ua=True)
        else:
            geturl = response.meta['get_url']
            url = geturl.get_start_url()
            geturl.close()
            geturl = get_url()
            geturl.open_url(url)
            yield self.get_request(geturl,max_behot_time=0,ua=True)


    def parse_wenda(self, response):
        text = response.text
        new_item = wenda()
        new_item['new_id'] = response.meta['js']['item_id']
        new_item['new_url'] = response.meta['url']
        new_item['new_title'] = re.search(r'"title": ?"(.*?)",',text)[1]
        new_item['new_content'] = re.search(r"abstract: ?'(.*?)',",text)[1]
        yield new_item

    def parse_article(self, response):
        text = response.text
        new_item = news()
        new_item['new_id'] = response.meta['js']['item_id']
        new_item['new_url'] = response.meta['url']
        new_item['new_title'] = re.search(r"title: ?(.+)',",text)[1]
        new_item['new_content'] = re.search(r"content: ?(.+)',",text)[1]
        new_item['new_from'] = re.search(r"source: ?(.+)',",text)[1]
        new_item['new_time'] = re.search(r"time: ?(.+)'",text)[1]
        yield new_item