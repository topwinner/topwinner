'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class SpmeffectGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.date = None
		self.module_detail = None
		self.page_detail = None

	def getapiname(self):
		return 'taobao.spmeffect.get'
