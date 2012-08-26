'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class ShoprecommendItemsGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.count = None
		self.ext = None
		self.recommend_type = None
		self.seller_id = None

	def getapiname(self):
		return 'taobao.shoprecommend.items.get'
