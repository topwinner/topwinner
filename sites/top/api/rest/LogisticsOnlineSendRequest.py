'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class LogisticsOnlineSendRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.cancel_id = None
		self.company_code = None
		self.feature = None
		self.out_sid = None
		self.sender_id = None
		self.tid = None

	def getapiname(self):
		return 'taobao.logistics.online.send'
