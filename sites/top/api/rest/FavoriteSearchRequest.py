'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class FavoriteSearchRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.collect_type = None
		self.page_no = None

	def getapiname(self):
		return 'taobao.favorite.search'
