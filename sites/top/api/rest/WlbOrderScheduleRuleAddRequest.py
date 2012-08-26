'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class WlbOrderScheduleRuleAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.backup_store_id = None
		self.default_store_id = None
		self.option = None
		self.prov_area_ids = None

	def getapiname(self):
		return 'taobao.wlb.order.schedule.rule.add'
