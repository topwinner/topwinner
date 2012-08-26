'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TripJipiaoAgentOrderSpecialConfirmRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.can_pay = None
		self.fail_memo = None
		self.fail_type = None
		self.order_id = None
		self.pay_latest_time = None

	def getapiname(self):
		return 'taobao.trip.jipiao.agent.order.special.confirm'
