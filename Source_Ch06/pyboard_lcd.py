# MicroPython for the IOT - Chapter 6
# Example module for the LCD skin on a Pyboard
#
# Note: The LCD is positioned in the "X" position.
#
import sys

# First, make sure this is running on a Pyboard
try:
    import pyb
except ImportError:
    print("ERROR: not on a Pyboard!")
    sys.exit(-1)

# Next, make sure the LCD skin library in the firmware
try:
    import lcd160cr
except ImportError:
    print("ERROR: LCD160CR library missing!")
    sys.exit(-1)

# Return color of LED
def led_color(num):
    if num == 1: return "red"
    elif num == 2: return "green"
    elif num == 3: return "orange"
    else: return "blue"

# Use a method to turn off last LED and the next one on
def turn_on_led(num, led_last):
    # turn last LED off
    led = pyb.LED(led_last)
    led.off()
    led = pyb.LED(num)
    led.on()
    sys.stdout.write("Turning off ")
    sys.stdout.write(led_color(led_last))
    sys.stdout.write(" - Turning on ")
    sys.stdout.write(led_color(num))
    sys.stdout.write("\n")

# Setup the LCD in the "X" position
lcd = lcd160cr.LCD160CR('X')

for j in range(1, 4):   # Turn off all of the LEDs
    led = pyb.LED(j)    # Get the LED
    led.off()           # Turn the LED off

# Now, let's play a game. Let's change the LEDs to
# different colors depending on where the user touches
# the screen.
print("Welcome to the touch screen demo!")
print("Touch the screen in the corners to change the LED lit.")
print("Touch the center to exit.")
center = False
last_led = 1
while not center:
    pyb.delay(50)
    if lcd.is_touched:
        touch = lcd.get_touch()
        if (touch[0] == 0):
            continue
        # Upper-left corner
        if ((touch[1] <= 60) and (touch[2] <= 60)):
            turn_on_led(1, last_led)
            last_led = 1
        # Upper-right corner
        elif ((touch[1] >= 100) and (touch[2] <= 60)):
            turn_on_led(2, last_led)
            last_led = 2
        # Lower-right corner
        elif ((touch[1] >= 100) and (touch[2] >= 100)):
            turn_on_led(3, last_led)
            last_led = 3
        # Lower-left corner
        elif ((touch[1] <= 60) and (touch[2] >= 100)):
            turn_on_led(4, last_led)
            last_led = 4
        # Center
        elif ((touch[1] > 60) and (touch[1] < 100) and (touch[2] > 60) and (touch[2] < 100)):
            led = pyb.LED(last_led)
            led.off()
            center = True

print("Thanks for playing!")
sys.exit(0)
