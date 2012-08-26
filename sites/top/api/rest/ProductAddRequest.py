'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class ProductAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.binds = None
		self.cid = None
		self.customer_props = None
		self.desc = None
		self.image = None
		self.major = None
		self.market_time = None
		self.name = None
		self.outer_id = None
		self.price = None
		self.property_alias = None
		self.props = None
		self.sale_props = None

	def getapiname(self):
		return 'taobao.product.add'
