'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class SimbaInsightCatsanalysisGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.category_ids = None
		self.nick = None
		self.stu = None

	def getapiname(self):
		return 'taobao.simba.insight.catsanalysis.get'
