'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class WlbOutInventoryChangeNotifyRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.change_count = None
		self.item_id = None
		self.op_type = None
		self.order_source_code = None
		self.out_biz_code = None
		self.result_count = None
		self.source = None
		self.store_code = None
		self.type = None

	def getapiname(self):
		return 'taobao.wlb.out.inventory.change.notify'
