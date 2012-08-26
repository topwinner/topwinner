'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TradeConfirmfeeGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.is_detail = None
		self.tid = None

	def getapiname(self):
		return 'taobao.trade.confirmfee.get'
