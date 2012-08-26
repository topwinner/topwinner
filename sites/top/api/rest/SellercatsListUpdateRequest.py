'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class SellercatsListUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.cid = None
		self.name = None
		self.pict_url = None
		self.sort_order = None

	def getapiname(self):
		return 'taobao.sellercats.list.update'
