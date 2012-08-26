'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class ItemImgUploadRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.image = None
		self.is_major = None
		self.num_iid = None
		self.position = None

	def getapiname(self):
		return 'taobao.item.img.upload'
