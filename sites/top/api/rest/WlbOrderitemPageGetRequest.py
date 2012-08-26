'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class WlbOrderitemPageGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.order_code = None
		self.page_no = None
		self.page_size = None

	def getapiname(self):
		return 'taobao.wlb.orderitem.page.get'
