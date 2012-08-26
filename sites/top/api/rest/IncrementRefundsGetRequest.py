'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class IncrementRefundsGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.end_modified = None
		self.nick = None
		self.page_no = None
		self.page_size = None
		self.start_modified = None
		self.status = None

	def getapiname(self):
		return 'taobao.increment.refunds.get'
