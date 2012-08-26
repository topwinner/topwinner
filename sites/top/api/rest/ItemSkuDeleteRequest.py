'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class ItemSkuDeleteRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.item_num = None
		self.item_price = None
		self.lang = None
		self.num_iid = None
		self.properties = None

	def getapiname(self):
		return 'taobao.item.sku.delete'
