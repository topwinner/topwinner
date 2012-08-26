'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TradeOrderskuUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.oid = None
		self.sku_id = None
		self.sku_props = None

	def getapiname(self):
		return 'taobao.trade.ordersku.update'
