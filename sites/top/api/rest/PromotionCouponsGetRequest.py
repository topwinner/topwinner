'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class PromotionCouponsGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.coupon_id = None
		self.denominations = None
		self.end_time = None
		self.page_no = None
		self.page_size = None

	def getapiname(self):
		return 'taobao.promotion.coupons.get'
