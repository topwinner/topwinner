'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class HotelOrderFaceCheckRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.checked = None
		self.checkin_date = None
		self.checkout_date = None
		self.oid = None

	def getapiname(self):
		return 'taobao.hotel.order.face.check'
