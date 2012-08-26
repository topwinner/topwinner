'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class WangwangEserviceChatlogGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.end_date = None
		self.from_id = None
		self.start_date = None
		self.to_id = None

	def getapiname(self):
		return 'taobao.wangwang.eservice.chatlog.get'
