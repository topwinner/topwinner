'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TopatsIncrementMessagesGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.end = None
		self.start = None
		self.topics = None

	def getapiname(self):
		return 'taobao.topats.increment.messages.get'
