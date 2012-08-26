'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class WlbItemSynchronizeRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.ext_entity_id = None
		self.ext_entity_type = None
		self.item_id = None
		self.user_nick = None

	def getapiname(self):
		return 'taobao.wlb.item.synchronize'
