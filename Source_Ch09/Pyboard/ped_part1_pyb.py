# MicroPython for the IOT - Chapter 9
#
# Project 2: A MicroPython Pedestrian Crosswalk Simulator
#            Part 1 - controlling LEDs and button as input
#
# Required Components:
# - Pyboard
# - (2) Red LEDs
# - (2) Yellow LEDs
# - (1) Green LED
# - (5) 220 Ohm resistors
# - (1) breadboard friendly momentary button
#
# Note: this only runs on the Pyboard.
#
# Imports for the project
from pyb import Pin, delay, ExtInt

# Setup the button and LEDs
button = Pin('X1', Pin.IN, Pin.PULL_UP)
led1 = Pin('X7', Pin.OUT_PP)
led2 = Pin('X6', Pin.OUT_PP)
led3 = Pin('X5', Pin.OUT_PP)
led4 = Pin('X4', Pin.OUT_PP)
led5 = Pin('X3', Pin.OUT_PP)

# Setup lists for the LEDs
stoplight = [led1, led2, led3]
walklight = [led4, led5]

# Turn off the LEDs
for led in stoplight:
    led.low()
for led in walklight:
    led.low()

# Start with green stoplight and red walklight
stoplight[2].high()
walklight[0].high()

# We need a method to cycle the stoplight and walklight
#
# We toggle from green to yellow for 2 seconds
# then red for 20 seconds.
def cycle_lights():
    # Go yellow.
    stoplight[2].low()
    stoplight[1].high()
    # Wait 2 seconds
    delay(2000)
    # Go red and turn on walk light
    stoplight[1].low()
    stoplight[0].high()
    delay(500)  # Give the pedestrian a chance to see it
    walklight[0].low()
    walklight[1].high()
    # After 10 seconds, start blinking the walk light
    delay(10000)
    for i in range(0,10):
        walklight[1].low()
        delay(500)
        walklight[1].high()
        delay(500)
        
    # Stop=green, walk=red
    walklight[1].low()
    walklight[0].high()
    delay(500)  # Give the pedestrian a chance to see it
    stoplight[0].low()
    stoplight[2].high()

# Create callback for the button
def button_pressed(line):
    cur_value = button.value()
    active = 0
    while (active < 50):
        if button.value() != cur_value:
            active += 1
        else:
            active = 0
        delay(1)
        print("")
    if active:
        cycle_lights()
    else:
        print("False press")        

# Create an interrupt for the button
e = ExtInt('X1', ExtInt.IRQ_FALLING, Pin.PULL_UP, button_pressed)

