'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class WlbOrderscheduleruleDeleteRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.user_nick = None

	def getapiname(self):
		return 'taobao.wlb.orderschedulerule.delete'
