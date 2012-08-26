'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TradesSoldGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.end_created = None
		self.ext_type = None
		self.fields = None
		self.page_no = None
		self.page_size = None
		self.rate_status = None
		self.start_created = None
		self.status = None
		self.tag = None
		self.type = None
		self.use_has_next = None

	def getapiname(self):
		return 'taobao.trades.sold.get'
