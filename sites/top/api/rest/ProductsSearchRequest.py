'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class ProductsSearchRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.cid = None
		self.fields = None
		self.page_no = None
		self.page_size = None
		self.props = None
		self.q = None
		self.status = None
		self.vertical_market = None

	def getapiname(self):
		return 'taobao.products.search'
