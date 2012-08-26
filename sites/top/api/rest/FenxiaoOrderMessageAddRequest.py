'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class FenxiaoOrderMessageAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.message = None
		self.purchase_order_id = None

	def getapiname(self):
		return 'taobao.fenxiao.order.message.add'
