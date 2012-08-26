'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TopatsItemcatsGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.cids = None
		self.output_format = None
		self.seller_type = None

	def getapiname(self):
		return 'taobao.topats.itemcats.get'
