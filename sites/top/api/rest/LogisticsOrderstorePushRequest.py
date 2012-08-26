'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class LogisticsOrderstorePushRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.occure_time = None
		self.operate_detail = None
		self.operator_contact = None
		self.operator_name = None
		self.trade_id = None

	def getapiname(self):
		return 'taobao.logistics.orderstore.push'
