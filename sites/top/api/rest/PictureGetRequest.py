'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class PictureGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.deleted = None
		self.end_date = None
		self.modified_time = None
		self.order_by = None
		self.page_no = None
		self.page_size = None
		self.picture_category_id = None
		self.picture_id = None
		self.start_date = None
		self.title = None

	def getapiname(self):
		return 'taobao.picture.get'
