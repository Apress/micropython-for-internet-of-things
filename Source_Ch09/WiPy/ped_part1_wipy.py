# MicroPython for the IOT - Chapter 9
#
# Project 2: A MicroPython Pedestrian Crosswalk Simulator
#            Part 1 - controlling LEDs and button as input
#
# Required Components:
# - WiPy
# - (2) Red LEDs
# - (2) Yellow LEDs
# - (1) Green LED
# - (5) 220 Ohm resistors
# - (1) breadboard friendly momentary button
#
# Note: this only runs on the WiPy.
#
# Imports for the project
from machine import Pin
import utime

# Setup the button and LEDs
button = Pin('P23', Pin.IN, Pin.PULL_UP)
led1 = Pin('P3', Pin.OUT)
led2 = Pin('P4', Pin.OUT)
led3 = Pin('P5', Pin.OUT)
led4 = Pin('P6', Pin.OUT)
led5 = Pin('P7', Pin.OUT)

# Setup lists for the LEDs
stoplight = [led1, led2, led3]
walklight = [led4, led5]

# Turn off the LEDs
for led in stoplight:
    led.value(0)
for led in walklight:
    led.value(0)

# Start with green stoplight and red walklight
stoplight[2].value(1)
walklight[0].value(1)

# We need a method to cycle the stoplight and walklight
#
# We toggle from green to yellow for 2 seconds
# then red for 20 seconds.
def cycle_lights():
    # Go yellow.
    stoplight[2].value(0)
    stoplight[1].value(1)
    # Wait 2 seconds
    utime.sleep(2)
    # Go red and turn on walk light
    stoplight[1].value(0)
    stoplight[0].value(1)
    utime.sleep_ms(500)  # Give the pedestrian a chance to see it
    walklight[0].value(0)
    walklight[1].value(1)
    # After 10 seconds, start blinking the walk light
    utime.sleep(1)
    for i in range(0,10):
        walklight[1].value(0)
        utime.sleep_ms(500)
        walklight[1].value(1)
        utime.sleep_ms(500)
        
    # Stop=green, walk=red
    walklight[1].value(0)
    walklight[0].value(1)
    utime.sleep_ms(500)  # Give the pedestrian a chance to see it
    stoplight[0].value(0)
    stoplight[2].value(1)

# Create callback for the button
def button_pressed(line):
    cur_value = button.value()
    active = 0
    while (active < 50):
        if button.value() != cur_value:
            active += 1
        else:
            active = 0
        utime.sleep_ms(1)
        print("")
    if active:
        cycle_lights()
    else:
        print("False press")        

# Create an interrupt for the button
button.callback(Pin.IRQ_FALLING, button_pressed)

