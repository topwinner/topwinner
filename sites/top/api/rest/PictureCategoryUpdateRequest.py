'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class PictureCategoryUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.category_id = None
		self.category_name = None
		self.parent_id = None

	def getapiname(self):
		return 'taobao.picture.category.update'
