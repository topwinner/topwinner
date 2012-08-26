'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class AlipayUserAccountFreezeGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.freeze_type = None

	def getapiname(self):
		return 'alipay.user.account.freeze.get'
