'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class HotelRoomsSearchRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.gids = None
		self.hids = None
		self.item_ids = None
		self.need_hotel = None
		self.need_room_desc = None
		self.need_room_quotas = None
		self.need_room_type = None
		self.page_no = None
		self.rids = None

	def getapiname(self):
		return 'taobao.hotel.rooms.search'
