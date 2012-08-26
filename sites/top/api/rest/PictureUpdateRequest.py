'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class PictureUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.new_name = None
		self.picture_id = None

	def getapiname(self):
		return 'taobao.picture.update'
