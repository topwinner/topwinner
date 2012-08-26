'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class PictureCategoryAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.parent_id = None
		self.picture_category_name = None

	def getapiname(self):
		return 'taobao.picture.category.add'
