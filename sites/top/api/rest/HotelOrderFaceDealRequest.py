'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class HotelOrderFaceDealRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.oid = None
		self.oper_type = None
		self.reason_text = None
		self.reason_type = None

	def getapiname(self):
		return 'taobao.hotel.order.face.deal'
