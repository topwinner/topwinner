'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class DeliveryTemplateGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.template_ids = None
		self.user_nick = None

	def getapiname(self):
		return 'taobao.delivery.template.get'
