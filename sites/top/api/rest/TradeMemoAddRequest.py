'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TradeMemoAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.flag = None
		self.memo = None
		self.tid = None

	def getapiname(self):
		return 'taobao.trade.memo.add'
