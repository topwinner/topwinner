'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class SimbaAdgroupAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.campaign_id = None
		self.default_price = None
		self.img_url = None
		self.item_id = None
		self.nick = None
		self.title = None

	def getapiname(self):
		return 'taobao.simba.adgroup.add'
