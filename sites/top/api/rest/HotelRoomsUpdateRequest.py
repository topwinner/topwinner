'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class HotelRoomsUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.gid_room_quota_map = None
		self.multi_room_quotas = None

	def getapiname(self):
		return 'taobao.hotel.rooms.update'
