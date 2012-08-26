'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TaobaokeListurlGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.nick = None
		self.outer_code = None
		self.pid = None
		self.q = None

	def getapiname(self):
		return 'taobao.taobaoke.listurl.get'
