import datetime
from mongoengine import *


class User(Document):
	meta={"collection" : "Users",
	      "indexes":[
			"email"
			]}

	email = EmailField(required = True, unique = True)
	first_name = StringField(required = True)
	last_name = StringField(required = True)
	gender = StringField(required = False, default = "u")


#class Car(Document):

class Track(Document):
	name = StringField(required = True, unique = True)


class Sensor(EmbeddedDocument):
	time = IntField(required= False) #tRUE

class FloatSensor(Sensor):
	value = DecimalField(required = True, default=0.0) #TZE TOUTO

class IntegerSensor(Sensor):
	value = IntField(required = True, default = 0)

class BooleanSensor(Sensor):
	value = BooleanField(required = True, default = 0) #SASTO GMT SHISTON

class Model(Document): 
	meta={"collection" : "model",
	      "indexes":[
			"driver"
			]}
	driver = ReferenceField(User)
	track = ReferenceField(Track)
	created = DateTimeField(required = True, default = datetime.datetime.utcnow)
	gas = ListField(EmbeddedDocumentField(FloatSensor), default = list)
	brake = ListField(EmbeddedDocumentField(FloatSensor), default = list)
	clutch = ListField(EmbeddedDocumentField(FloatSensor), default = list)
	gear = ListField(EmbeddedDocumentField(IntegerSensor), default = list)
	speed = ListField(EmbeddedDocumentField(FloatSensor), default = list)
	intrack = ListField(EmbeddedDocumentField(IntegerSensor), default = list)
	distance = ListField(EmbeddedDocumentField(FloatSensor), default = list)
	#position
	
	def add_data(self,data,in_track): #Speed,brakes,gas,clutch,gear,distance,time
		speed = FloatSensor()
		brake = FloatSensor()
		gas = FloatSensor()
		clutch = FloatSensor()
		gear = IntegerSensor()
		intrack = IntegerSensor()#tzetouto
		distance = FloatSensor()

		time = data[6]

		speed.value = data[0]
		speed.time = time
		self.speed.append(speed)
		
		brake.value = data[1]
		brake.time = time
		self.brake.append(brake)

		gas.value = data[2]
		gas.time = time
		self.gas.append(gas)

		clutch.value = data[3]
		clutch.time = time
		self.clutch.append(clutch)

		gear.value = data[4]
		gear.time = time
		self.gear.append(gear)

		intrack.value = in_track
		intrack.time = time
		self.intrack.append(intrack)	
		
		distance.value= data[5]
		distance.time = time
		self.distance.append(distance)	

		self.save()


				

	



