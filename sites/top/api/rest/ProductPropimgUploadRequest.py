'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class ProductPropimgUploadRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.image = None
		self.position = None
		self.product_id = None
		self.props = None

	def getapiname(self):
		return 'taobao.product.propimg.upload'
