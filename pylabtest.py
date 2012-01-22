import sys
sys.path.append("/home/the0project/Desktop/ProjectSimulator/python_db")
from db_model import * 
import db_connect
import math
import pylab

#x_list = pylab.arange(0.0, 5.0, 0.01)

pylab.figure(1)

email_s = raw_input("Enter Email: ")
user = User.objects(email = email_s).get()
model = Model.objects(driver = user).get()

data =[]
for s in model.speed:
	x=  float (s.value)
	data.append(x)

pylab.subplot(331)
y_speed = data
pylab.xlabel("time")
pylab.ylabel("speed")
pylab.plot(y_speed, 'b')

data =[]
for s in model.brake:
	x=  float (s.value)
	data.append(x)
pylab.subplot(332)
y_brake = data
pylab.xlabel("time")
pylab.ylabel("brake")
pylab.plot(y_brake, 'b')


data =[]
for s in model.gas:
	x=  float (s.value)
	data.append(x)
pylab.subplot(333)
y_gas = data
pylab.xlabel("time")
pylab.ylabel("gas")
pylab.plot(y_gas, 'b')


data =[]
for s in model.gear:
	x=  float (s.value)
	data.append(x)
pylab.subplot(334)
y_gear = data
pylab.xlabel("time")
pylab.ylabel("gear")
pylab.plot(y_gear, 'b')

data =[]
for s in model.distance:
	x=  float (s.value)
	data.append(x)
pylab.subplot(335)
y_gear = data
pylab.xlabel("time")
pylab.ylabel("distance")
pylab.plot(y_gear, 'b')

data =[]
for s in model.intrack:
	x=  float (s.value)
	data.append(x)
pylab.subplot(336)
y_gear = data
pylab.xlabel("time")
pylab.ylabel("intrack")
pylab.plot(y_gear, 'b')


pylab.show()
