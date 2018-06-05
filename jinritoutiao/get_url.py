from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
import re
import time
from jinritoutiao import RandomUserAgent

class get_url(object):
	"""docstring for get_url"""
	def __init__(self):
		super(get_url, self).__init__()
		dcap = dict(DesiredCapabilities.PHANTOMJS)
		self.user_agent =  RandomUserAgent.get_useragent()
		dcap["phantomjs.page.settings.userAgent"] = self.user_agent 
		self.dri = webdriver.PhantomJS(desired_capabilities=dcap)

	def open_url(self,url):
		self.url = url
		self.dri.get(url)
		time.sleep(3)
		self.set_cookie()

	def close(self):
		self.dri.close()

	def get_start_url(self):
		return self.url

	def get_user_agent(self):
		return self.user_agent

	def get_cookie(self):
		return self.cookie

	def get_url(self,max_behot_time):
		category = self.get_category()
		ascp = self.get_as_cp()
		signature = self.get_signature(max_behot_time)
		url = "https://www.toutiao.com/api/pc/feed/?category="+category+"&utm_source=toutiao&widen=1&max_behot_time="+max_behot_time+"&max_behot_time_tmp="+max_behot_time+"&tadrequire=true&as="+ascp['as']+"&cp="+ascp['cp']+"&_signature="+signature
		return url

	def get_category(self):
		res = re.search(r'/ch/(.*?)/$',self.url)
		return res.group(1)

	def get_as_cp(self):
		ascp = self.dri.execute_script('return ascp.getHoney()')
		return ascp

	def get_signature(self,max_behot_time):
		signature = self.dri.execute_script('return TAC.sign('+max_behot_time+')')
		return signature

	def set_cookie(self):
		self.cookie = {}
		for x in self.dri.get_cookies():
			self.cookie[x['name']] = x['value']
