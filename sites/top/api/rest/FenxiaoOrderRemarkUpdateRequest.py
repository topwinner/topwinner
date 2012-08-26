'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class FenxiaoOrderRemarkUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.purchase_order_id = None
		self.supplier_memo = None
		self.supplier_memo_flag = None

	def getapiname(self):
		return 'taobao.fenxiao.order.remark.update'
