'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class HotelRoomAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.area = None
		self.bbn = None
		self.bed_type = None
		self.breakfast = None
		self.deposit = None
		self.desc = None
		self.fee = None
		self.guide = None
		self.hid = None
		self.multi_room_quotas = None
		self.payment_type = None
		self.pic = None
		self.pic_path = None
		self.price_type = None
		self.rid = None
		self.room_quotas = None
		self.service = None
		self.site_param = None
		self.size = None
		self.storey = None
		self.title = None

	def getapiname(self):
		return 'taobao.hotel.room.add'
