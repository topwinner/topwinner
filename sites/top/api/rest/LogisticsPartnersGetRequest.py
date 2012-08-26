'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class LogisticsPartnersGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.goods_value = None
		self.is_need_carriage = None
		self.service_type = None
		self.source_id = None
		self.target_id = None

	def getapiname(self):
		return 'taobao.logistics.partners.get'
