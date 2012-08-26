'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class HotelNameGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.city = None
		self.country = None
		self.district = None
		self.domestic = None
		self.name = None
		self.province = None

	def getapiname(self):
		return 'taobao.hotel.name.get'
