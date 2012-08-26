'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class MarketingPromotionsGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.num_iid = None
		self.status = None
		self.tag_id = None

	def getapiname(self):
		return 'taobao.marketing.promotions.get'
