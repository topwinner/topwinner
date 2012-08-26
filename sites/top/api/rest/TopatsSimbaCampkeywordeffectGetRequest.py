'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class TopatsSimbaCampkeywordeffectGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.campaign_id = None
		self.nick = None
		self.search_type = None
		self.source = None
		self.time_slot = None

	def getapiname(self):
		return 'taobao.topats.simba.campkeywordeffect.get'
