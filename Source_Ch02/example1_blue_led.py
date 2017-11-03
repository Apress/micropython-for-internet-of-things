#
# MicroPython for the IOT
# 
# Example 1
#
# Turn on the blue LED (4 = Blue)
#
# Dr. Charles Bell
#
import pyb              # Import the Pyboard library

led = pyb.LED(4)        # Get the LED instance
led.off()               # Make sure it's off first
    
for i in range(1, 20):  # Run the indented code 20 times
    led.on()            # Turn LED on
    pyb.delay(250)      # Wait for 250 milleseconds
    led.off()           # Turn LED off
    pyb.delay(250)      # Wait for 250 milleseconds

led.off()               # Turn the LED off at the end
print("Done!")          # Goodbye!
