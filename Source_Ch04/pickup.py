#
# MicroPython for the IOT
# 
# Class Example: Exeercising the PickupTruck class.
#
# Dr. Charles Bell
#
from pickup_truck import PickupTruck

pickup = PickupTruck(500)
pickup.add_occupant()
pickup.add_occupant()
pickup.add_occupant()
pickup.add_occupant()
pickup.add_payload(100)
pickup.add_payload(300)
print("Number of occupants in truck = {0}.".format(pickup.num_occupants()))
print("Weight in truck = {0}.".format(pickup.get_payload()))
pickup.add_payload(200)
pickup.remove_payload(400)
pickup.remove_payload(10)

print("PickupTruck.__doc__:", PickupTruck.__doc__)
print("PickupTruck.__name__:", PickupTruck.__name__)
print("PickupTruck.__module__:", PickupTruck.__module__)
print("PickupTruck.__bases__:", PickupTruck.__bases__)
print("PickupTruck.__dict__:", PickupTruck.__dict__)

