'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class WangwangEserviceChatpeersGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.charset = None
		self.chat_id = None
		self.end_date = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.wangwang.eservice.chatpeers.get'
