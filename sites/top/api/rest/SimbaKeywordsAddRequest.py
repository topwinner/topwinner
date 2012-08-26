'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class SimbaKeywordsAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.adgroup_id = None
		self.keyword_prices = None
		self.nick = None

	def getapiname(self):
		return 'taobao.simba.keywords.add'
