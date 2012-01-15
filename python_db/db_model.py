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
	time = IntField(required= True) 

class FloatSensor(Sensor):
	value = FloatField(required = True)

class IntegerSensor(Sensor):
	value = IntField(required = True, default = 0)
	time = IntField(required = True)

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



