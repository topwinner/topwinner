'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TripJipiaoAgentOrderSearchRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.begin_time = None
		self.end_time = None
		self.has_itinerary = None
		self.page = None
		self.status = None
		self.trip_type = None

	def getapiname(self):
		return 'taobao.trip.jipiao.agent.order.search'
