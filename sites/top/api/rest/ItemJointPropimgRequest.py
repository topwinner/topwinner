'''
Created by auto_sdk on 2012-08-26 16:43:44
'''
from top.api.base import RestApi
class ItemJointPropimgRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.num_iid = None
		self.pic_path = None
		self.position = None
		self.properties = None

	def getapiname(self):
		return 'taobao.item.joint.propimg'
