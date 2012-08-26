'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class ProductGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.cid = None
		self.fields = None
		self.product_id = None
		self.props = None

	def getapiname(self):
		return 'taobao.product.get'
