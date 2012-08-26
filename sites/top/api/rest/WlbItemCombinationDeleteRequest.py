'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class WlbItemCombinationDeleteRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.dest_item_list = None
		self.item_id = None

	def getapiname(self):
		return 'taobao.wlb.item.combination.delete'
