'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TopatsDeliverySendRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.company_codes = None
		self.memos = None
		self.order_types = None
		self.out_sids = None
		self.seller_address = None
		self.seller_area_id = None
		self.seller_mobile = None
		self.seller_name = None
		self.seller_phone = None
		self.seller_zip = None
		self.tids = None

	def getapiname(self):
		return 'taobao.topats.delivery.send'
