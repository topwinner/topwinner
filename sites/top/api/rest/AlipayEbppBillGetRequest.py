'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class AlipayEbppBillGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.auth_token = None
		self.merchant_order_no = None
		self.order_type = None

	def getapiname(self):
		return 'alipay.ebpp.bill.get'
