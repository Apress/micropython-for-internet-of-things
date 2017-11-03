# MicroPython for the IOT - Chapter 6
# Simple example for working with interrupts using a class
# to store state.
#
import sys

# First, make sure this is running on a Pyboard
try:
    import pyb
except ImportError:
    print("ERROR: not on a Pyboard!")
    sys.exit(-1)

# Initiate the switch class
switch = pyb.Switch()

class Cycle_LED(object):
    # Constructor
    def __init__(self, sw):
        self.cur_led = 0
        sw.callback(self.do_switch_press)

    # Switch callback function
    def do_switch_press(self):#
        # Turn off the last led unless this is the first time through the cycle
        if self.cur_led > 0:
            pyb.LED(self.cur_led).off()
        if self.cur_led < 4:
            self.cur_led = self.cur_led + 1
        else:
            self.cur_led = 1
        # Turn on the next led
        pyb.LED(self.cur_led).on()

# Initiate the Cycle_LED class and setup the callback
cycle = Cycle_LED(switch)

# Now, simulate doing something else
print("Testing the switch callback. Press CTRL-C to quit.")
while True:
    sys.stdout.write(".")  # Print something to show we're still in the loop
    pyb.delay(1000)        # Wait a second...

