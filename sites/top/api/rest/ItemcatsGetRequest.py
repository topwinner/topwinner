'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class ItemcatsGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.cids = None
		self.fields = None
		self.parent_cid = None

	def getapiname(self):
		return 'taobao.itemcats.get'
