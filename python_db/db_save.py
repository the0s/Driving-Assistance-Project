from db_connect import *
from mongoengine import *

class SaveDB:
	def _saveModel(self,data,model):
		data = data.split(';')
		print data		
		model.add_data(data)

		
	def _saveUser(self,user):
		print user
			




    
