'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class UmpRangeAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.act_id = None
		self.ids = None
		self.type = None

	def getapiname(self):
		return 'taobao.ump.range.add'
