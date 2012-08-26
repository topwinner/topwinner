'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TripJipiaoAgentItinerarySendRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.company_code = None
		self.express_code = None
		self.itinerary_id = None
		self.itinerary_no = None
		self.send_date = None

	def getapiname(self):
		return 'taobao.trip.jipiao.agent.itinerary.send'
