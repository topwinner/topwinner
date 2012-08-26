'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class LogisticsAddressRemoveRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.contact_id = None

	def getapiname(self):
		return 'taobao.logistics.address.remove'
