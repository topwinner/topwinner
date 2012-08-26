'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class PromotionCoupondetailGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.coupon_id = None
		self.page_no = None
		self.page_size = None
		self.state = None

	def getapiname(self):
		return 'taobao.promotion.coupondetail.get'
