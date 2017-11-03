#
# MicroPython for the IOT
# 
# Example 2
#
# Turn on the four LEDs on the board in order
#
# 1 = Red
# 2 = Green
# 3 = Orange
# 4 = Blue
#
# Dr. Charles Bell
#
import pyb              # Import the Pyboard library

for j in range(1, 4):   # Turn off all of the LEDs
    led = pyb.LED(j)    # Get the LED
    led.off()           # Turn the LED off
    
i = 1                   # LED counter
while True:             # Loop forever
    led = pyb.LED(i)    # Get next LED  
    led.on()            # Turn LED on
    pyb.delay(500)      # Wait for 1/2 second
    led.off()           # Turn LED off
    pyb.delay(500)      # Wait for 1/2 second
    i = i + 1           # Increment the LED counter
    if i > 4:           # If > 4, start over at 1
        i = 1
        
