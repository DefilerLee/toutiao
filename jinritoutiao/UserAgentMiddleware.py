import random
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from jinritoutiao import RandomUserAgent


class RotateUserAgentMiddleware(UserAgentMiddleware):
    def process_request(self, request, spider):
        """
        UserAgent中间件，产生随机UserAgent
        """
        ua = RandomUserAgent.get_useragent()
        if not ('ua' in request.meta):
            request.headers.setdefault('User-Agent', ua)
