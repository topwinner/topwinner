'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class SimbaKeywordsDeleteRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.campaign_id = None
		self.keyword_ids = None
		self.nick = None

	def getapiname(self):
		return 'taobao.simba.keywords.delete'
