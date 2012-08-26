'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class SellercatsListAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.name = None
		self.parent_cid = None
		self.pict_url = None
		self.sort_order = None

	def getapiname(self):
		return 'taobao.sellercats.list.add'
