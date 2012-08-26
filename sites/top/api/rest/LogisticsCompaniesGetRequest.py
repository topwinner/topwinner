'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class LogisticsCompaniesGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.is_recommended = None
		self.order_mode = None

	def getapiname(self):
		return 'taobao.logistics.companies.get'
