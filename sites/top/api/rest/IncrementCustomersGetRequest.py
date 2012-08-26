'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class IncrementCustomersGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.nicks = None
		self.page_no = None
		self.page_size = None
		self.type = None

	def getapiname(self):
		return 'taobao.increment.customers.get'
