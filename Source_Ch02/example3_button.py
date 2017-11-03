#
# MicroPython for the IOT
# 
# Example 3
#
# Flash the green LED when button is pushed
#
# Dr. Charles Bell
#
import pyb                  # Import the Pyboard library
led = pyb.LED(2)            # Get LED instance (2 = green)
led.off()                   # Make sure the LED if off

# Setup a callback function to handle button pressed
# using an interrupt service routine
def flash_led():
    for i in range(1, 25):
        led.on()
        pyb.delay(100)
        led.off()
        pyb.delay(100)

button = pyb.Switch()       # Get the button (switch)
button.callback(flash_led)  # Register the callback (ISR)

print("Ready for testing!")

