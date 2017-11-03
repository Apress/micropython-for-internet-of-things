# MicroPython for the IOT - Chapter 5
# Example module for the my_helper library

# This function converts values read from the sensor to a
# string for use in qualifying the moisture level read.

# Constants - adjust to "tune" your sensor

_UPPER_BOUND = 400
_LOWER_BOUND = 250

def get_moisture_level(raw_value):
    if raw_value <= _LOWER_BOUND:
        return("dry")
    elif raw_value >= _UPPER_BOUND:
        return("wet")
    return("ok")


