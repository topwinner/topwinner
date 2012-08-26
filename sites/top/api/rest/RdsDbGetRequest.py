'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class RdsDbGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.db_status = None
		self.instance_name = None

	def getapiname(self):
		return 'taobao.rds.db.get'
