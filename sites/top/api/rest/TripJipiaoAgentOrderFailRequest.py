'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TripJipiaoAgentOrderFailRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.fail_memo = None
		self.fail_type = None
		self.order_id = None

	def getapiname(self):
		return 'taobao.trip.jipiao.agent.order.fail'
