from db_model import * 
from server import *
from db_save import *

if __name__ == "__main__":
	UDP_IP = "192.168.1.98"
	UDP_PORT= 7011
	sock = Server(UDP_IP, UDP_PORT)
	
	'''
	user = User()
	user.first_name = "Test"
	user.last_name = "test"
	user.email = "email@lol.com"
	user.gender = "m"
	user.save()	
	'''
	user = User.objects(email = "email@lol.com").get()
	model = Model.objects(driver = user).get()
	#model = Model()
	#model.driver = user
	#model.save()
	
	
	while True:
		data, addr = sock.receive()
		print "Received Message From: ", addr[0],":",addr[1]
		print data
		print len(data)
		SaveDB()._saveModel(data, model)

