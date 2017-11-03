#
# MicroPython for the IOT
# 
# Class Example: Using the generic Vehicle class
#
# Dr. Charles Bell
#
from vehicle import Vehicle

sedan = Vehicle(2, 4)
sedan.add_occupant()
sedan.add_occupant()
sedan.add_occupant()
print("The car has {0} occupants.".format(sedan.num_occupants()))
