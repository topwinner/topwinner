'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class SimbaAdgroupNonsearchstatesUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.adgroupid_nonsearchstate_json = None
		self.campaign_id = None
		self.nick = None

	def getapiname(self):
		return 'taobao.simba.adgroup.nonsearchstates.update'
