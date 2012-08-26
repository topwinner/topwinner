'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class MarketingPromotionKfcRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.promotion_desc = None
		self.promotion_title = None

	def getapiname(self):
		return 'taobao.marketing.promotion.kfc'
