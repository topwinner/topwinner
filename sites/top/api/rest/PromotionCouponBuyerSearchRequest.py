'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class PromotionCouponBuyerSearchRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.page_no = None
		self.page_size = None
		self.seller_nick = None
		self.status = None

	def getapiname(self):
		return 'taobao.promotion.coupon.buyer.search'
