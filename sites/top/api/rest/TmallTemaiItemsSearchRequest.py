'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TmallTemaiItemsSearchRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.cat = None
		self.sort = None
		self.start = None

	def getapiname(self):
		return 'tmall.temai.items.search'
