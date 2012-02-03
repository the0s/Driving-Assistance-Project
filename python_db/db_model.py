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


class Car(Document):
	name = StringField(required = True, unique = True)

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

class Position3DSensor(Sensor):
	x = DecimalField(required = True, default=0.0)
	y = DecimalField(required = True, default=0.0)
	z = DecimalField(required = True, default=0.0)

class Model(Document): 
	meta={"collection" : "Models",
	      "indexes":[
			"driver"
			]}
	driver = ReferenceField(User)
	track = ReferenceField(Track)
	car = ReferenceField(Car)
	created = DateTimeField(required = True, default = datetime.datetime.utcnow)
	steering = ListField(EmbeddedDocumentField(FloatSensor), default = list)
	gas = ListField(EmbeddedDocumentField(FloatSensor), default = list)
	brake = ListField(EmbeddedDocumentField(FloatSensor), default = list)
	clutch = ListField(EmbeddedDocumentField(FloatSensor), default = list)
	gear = ListField(EmbeddedDocumentField(IntegerSensor), default = list)
	speed = ListField(EmbeddedDocumentField(FloatSensor), default = list)
	intrack = ListField(EmbeddedDocumentField(IntegerSensor), default = list)
	distance = ListField(EmbeddedDocumentField(FloatSensor), default = list)
	position = ListField(EmbeddedDocumentField(Position3DSensor),default = list)
	acceleration = ListField(EmbeddedDocumentField(Position3DSensor),default = list)
	
	def add_data(self,data,in_track): #Speed,brakes,gas,clutch,gear,distance,time, x, y ,z
		speed = FloatSensor()
		brake = FloatSensor()
		steering = FloatSensor()
		gas = FloatSensor()
		clutch = FloatSensor()
		gear = IntegerSensor()
		intrack = IntegerSensor()#tzetouto
		distance = FloatSensor()
		position = Position3DSensor() #tzetouto
		acc3d = Position3DSensor() #tzetouto

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

		position.time = time
		position.x = data[7]
		position.y = data[8]
		position.z = data[9]
		self.position.append(position)

		acc3d.time = time
		acc3d.x = data[10]
		acc3d.y = data[11]
		acc3d.z = data[12]
		self.acceleration.append(acc3d)

		steering.value = data[4]
		steering.time = time
		self.steering.append(steering)

		self.save()


				

	



