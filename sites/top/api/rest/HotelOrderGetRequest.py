'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class HotelOrderGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.need_guest = None
		self.need_message = None
		self.oid = None
		self.tid = None

	def getapiname(self):
		return 'taobao.hotel.order.get'
