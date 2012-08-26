'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TmallSelectedItemsSearchRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.cid = None

	def getapiname(self):
		return 'tmall.selected.items.search'
