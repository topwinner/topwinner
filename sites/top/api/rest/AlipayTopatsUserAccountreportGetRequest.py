'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class AlipayTopatsUserAccountreportGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.charset = None
		self.end_time = None
		self.fields = None
		self.start_time = None
		self.type = None

	def getapiname(self):
		return 'alipay.topats.user.accountreport.get'
