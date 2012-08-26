'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class SellercenterRoleAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.description = None
		self.name = None
		self.nick = None
		self.permission_codes = None

	def getapiname(self):
		return 'taobao.sellercenter.role.add'
