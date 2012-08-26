'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TripJipiaoAgentOrderSuccessRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.order_id = None
		self.success_info = None

	def getapiname(self):
		return 'taobao.trip.jipiao.agent.order.success'
