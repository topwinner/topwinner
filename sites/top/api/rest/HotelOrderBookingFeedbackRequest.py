'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class HotelOrderBookingFeedbackRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.failed_reason = None
		self.message_id = None
		self.oid = None
		self.out_oid = None
		self.refund_code = None
		self.result = None
		self.session_id = None

	def getapiname(self):
		return 'taobao.hotel.order.booking.feedback'
