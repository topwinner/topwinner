'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class CometDiscardinfoGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.end = None
		self.nick = None
		self.start = None
		self.types = None
		self.user_id = None

	def getapiname(self):
		return 'taobao.comet.discardinfo.get'
