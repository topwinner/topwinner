'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class SimbaInsightCatsbaseGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.category_ids = None
		self.filter = None
		self.nick = None
		self.time = None

	def getapiname(self):
		return 'taobao.simba.insight.catsbase.get'
