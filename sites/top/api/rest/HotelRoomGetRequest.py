'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class HotelRoomGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.gid = None
		self.item_id = None
		self.need_hotel = None
		self.need_room_desc = None
		self.need_room_quotas = None
		self.need_room_type = None

	def getapiname(self):
		return 'taobao.hotel.room.get'
