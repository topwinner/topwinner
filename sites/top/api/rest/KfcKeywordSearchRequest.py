'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class KfcKeywordSearchRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.apply = None
		self.content = None
		self.nick = None

	def getapiname(self):
		return 'taobao.kfc.keyword.search'