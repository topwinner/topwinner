'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class SimbaAdgroupCatmatchforecastGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.adgroup_id = None
		self.catmatch_price = None
		self.nick = None

	def getapiname(self):
		return 'taobao.simba.adgroup.catmatchforecast.get'
