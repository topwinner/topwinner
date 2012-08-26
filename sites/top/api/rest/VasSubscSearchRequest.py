'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class VasSubscSearchRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.article_code = None
		self.autosub = None
		self.end_deadline = None
		self.expire_notice = None
		self.item_code = None
		self.nick = None
		self.page_no = None
		self.page_size = None
		self.start_deadline = None
		self.status = None

	def getapiname(self):
		return 'taobao.vas.subsc.search'
