'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class WlbItemAuthorizationDeleteRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.authorize_id = None

	def getapiname(self):
		return 'taobao.wlb.item.authorization.delete'
