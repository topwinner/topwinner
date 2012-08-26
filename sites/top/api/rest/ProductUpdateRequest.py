'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class ProductUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.binds = None
		self.desc = None
		self.image = None
		self.major = None
		self.name = None
		self.native_unkeyprops = None
		self.outer_id = None
		self.price = None
		self.product_id = None
		self.sale_props = None

	def getapiname(self):
		return 'taobao.product.update'
