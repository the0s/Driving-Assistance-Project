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
	value = DecimalField(required = True, default=0.0)

class IntegerSensor(Sensor):
	value = IntField(required = True, default = 0)

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
	#position
	
	def add_data(self,data): #Speed,brakes,gas,clutch,gear
		speed = FloatSensor()
		brake = FloatSensor()
		gas = FloatSensor()
		clutch = FloatSensor()
		gear = IntegerSensor()

		speed.value = data[0]
		self.speed.append(speed)
		#self.speed.save()
		
		brake.value = data[1]
		self.speed.append(speed)
		#self.speed.save()

		gas.value = data[2]
		self.gas.append(gas)
		#self.gas.save()

		clutch.value = data[3]
		self.clutch.append(clutch)
		#self.clutch.save()
		
		gear.value = data[4]
		self.gear.append(gear)

		self.save()


				

	



