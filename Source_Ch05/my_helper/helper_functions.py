# MicroPython for the IOT - Chapter 5
# Example module for the my_helper library
# This module contains helper functions for general use.

try:
    import pyb
    _PYBOARD = True
except ImportError:
    import machine
    _PYBOARD = False

# Get a random number from 0-1 from a 2^24 bit random value
# if run on the WiPy, return 0-1 from a 2^30 bit random
# value if the Pyboard is used.
def get_rand():
    if _PYBOARD:
        return pyb.rng() / (2 ** 30 - 1)
    return machine.rng() / (2 ** 24 - 1)

# Format the time (epoch) for a better view
def format_time(tm_data):
    # Use a special shortcut to unpack tuple: *tm_data
    return "{0}-{1:0>2}-{2:0>2} {3:0>2}:{4:0>2}:{5:0>2}".format(*tm_data)
