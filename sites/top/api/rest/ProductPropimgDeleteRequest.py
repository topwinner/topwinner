'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class ProductPropimgDeleteRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.product_id = None

	def getapiname(self):
		return 'taobao.product.propimg.delete'
