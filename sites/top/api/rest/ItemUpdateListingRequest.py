'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class ItemUpdateListingRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.num = None
		self.num_iid = None

	def getapiname(self):
		return 'taobao.item.update.listing'
