'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class WlbInventoryDetailGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.inventory_type_list = None
		self.item_id = None
		self.store_code = None

	def getapiname(self):
		return 'taobao.wlb.inventory.detail.get'
