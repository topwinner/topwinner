'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class WangwangEserviceOnlinetimeGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.end_date = None
		self.service_staff_id = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.wangwang.eservice.onlinetime.get'
