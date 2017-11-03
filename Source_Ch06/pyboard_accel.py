# MicroPython for the IOT - Chapter 6
# Example for working with the accelerometer on a Pyboard
# Note: only works for the Pyboard!

import pyb
from pyb import Accel
acc = Accel()
print("Press CTRL-C to stop.")
while True:
    pyb.delay(500)    # Short delay before sampling
    print("X = {0:03} Y = {1:03} Z = {2:03}".format(acc.x(), acc.y(), acc.z()))
