'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class FenxiaoProductSkuUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.agent_cost_price = None
		self.dealer_cost_price = None
		self.product_id = None
		self.properties = None
		self.quantity = None
		self.sku_number = None
		self.standard_price = None

	def getapiname(self):
		return 'taobao.fenxiao.product.sku.update'
