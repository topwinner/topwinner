'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class SimbaToolsItemsTopGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.ip = None
		self.keyword = None
		self.nick = None

	def getapiname(self):
		return 'taobao.simba.tools.items.top.get'
