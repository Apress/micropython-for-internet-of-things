#
# MicroPython for the IOT
# 
# Class Example: A generic vehicle
#
# Dr. Charles Bell
#
class Vehicle:
    """Base class for defining vehicles"""
    axles = 0
    doors = 0
    occupants = 0

    def __init__(self, num_axles, num_doors):
        self.axles = num_axles
        self.doors = num_doors
    
    def get_axles(self):
        return self.axles
    
    def get_doors(self):
        return self.doors
    
    def add_occupant(self):
        self.occupants += 1
        
    def num_occupants(self):
        return self.occupants