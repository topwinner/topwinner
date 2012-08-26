'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class SkusQuantityUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.num_iid = None
		self.outerid_quantities = None
		self.skuid_quantities = None
		self.type = None

	def getapiname(self):
		return 'taobao.skus.quantity.update'
