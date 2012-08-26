'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class FenxiaoDiscountsGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.discount_id = None
		self.ext_fields = None

	def getapiname(self):
		return 'taobao.fenxiao.discounts.get'
