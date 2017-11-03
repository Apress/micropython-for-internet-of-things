#
# MicroPython for the IOT
# 
# Class Example: Inheriting the Vehicle class to form a
# model of a pickup truck with maximum occupants and maximum
# payload.
#
# Dr. Charles Bell
#
from vehicle import Vehicle

class PickupTruck(Vehicle):
    """This is a pickup truck that has:
    axles = 2,
    doors = 2,
    __max occupants = 3
    The maximum payload is set on instantiation.
    """
    occupants = 0
    payload = 0
    max_payload = 0
    __max_occupants = 3

    def __init__(self, max_weight):
        super().__init__(2,2)
        self.max_payload = max_weight
    
    def add_occupant(self):
        if (self.occupants < self.__max_occupants):
            super().add_occupant()
        else:
            print("Sorry, only 3 occupants are permitted in the truck.")
            
    def add_payload(self, num_pounds):
        if ((self.payload + num_pounds) < self.max_payload):
            self.payload += num_pounds
        else:
            print("Overloaded!")

    def remove_payload(self, num_pounds):
        if ((self.payload - num_pounds) >= 0):
            self.payload -= num_pounds
        else:
            print("Nothing in the truck.")
    
    def get_payload(self):
        return self.payload
            