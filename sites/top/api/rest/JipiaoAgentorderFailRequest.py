'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class JipiaoAgentorderFailRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.memo = None
		self.order_id = None
		self.reason = None

	def getapiname(self):
		return 'taobao.jipiao.agentorder.fail'
