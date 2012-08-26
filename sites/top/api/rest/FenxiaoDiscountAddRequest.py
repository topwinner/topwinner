'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class FenxiaoDiscountAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.discount_name = None
		self.discount_types = None
		self.discount_values = None
		self.target_ids = None
		self.target_types = None

	def getapiname(self):
		return 'taobao.fenxiao.discount.add'
