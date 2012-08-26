'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class RefundGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.refund_id = None

	def getapiname(self):
		return 'taobao.refund.get'
