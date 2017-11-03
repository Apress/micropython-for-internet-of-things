# MicroPython for the IOT - Chapter 9
#
# Project 2: A MicroPython Pedestrian Crosswalk Simulator
#            Part 2 - Controlling the walklight remotely
#
# Required Components:
# - Pyboard
# - (2) Red LEDs
# - (2) Yellow LEDs
# - (1) Green LED
# - (5) 220 Ohm resistors
# - (1) breadboard friendly momentary button
# - (1) CC3000 breakout board
#
# Note: this only runs on the Pyboard.
#
# Imports for the project
from pyb import Pin, delay, ExtInt, SPI
import network
import usocket as socket

# Setup network connection
nic = network.CC3K(SPI(2), Pin.board.Y5, Pin.board.Y4, Pin.board.Y3)
# Replace the following with yout SSID and password
nic.connect("YOUR_SSID", "YOUR_PASSWORD")
print("Connecting...")
while not nic.isconnected():
    delay(50)
print("Connected!")    
print("My IP address is: {0}".format(nic.ifconfig()[0]))

# HTML web page for the project
HTML_RESPONSE = """<!DOCTYPE html>
<html>
  <head>
    <title>MicroPython for the IOT - Project 2</title>
  </head>
  <center><h2>MicroPython for the IOT - Project 2</h2></center><br>
  <center>A simple project to demonstrate how to control hardware over the Internet.</center><br><br>
  <form>
    <center>
        <button name="WALK" value="PLEASE" type="submit" style="height: 50px; width: 100px">REQUEST WALK</button>
        <br><br>
        <button name="shutdown" value="now" type="submit" style="height: 50px; width: 100px">Stop Server</button>
    </center>
  </form>
</html>
"""

# Setup the LEDs
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

# Setup the socket and respond to HTML requests
def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 80))
    sock.listen(5)
    server_on = True
    while server_on:
        client, address = sock.accept()
        print("Got a connection from a client at: %s" % str(address))
        request = client.recv(1024)
        # Process the request from the client. Payload should appear in pos 6.
        # Check for walk button click
        walk_clicked = (request[:17] == b'GET /?WALK=PLEASE')
        # Check for stop server button click
        stop_clicked = (request[:18] == b'GET /?shutdown=now')
        if walk_clicked:
            print('Requesting walk now!')
            cycle_lights()
        elif stop_clicked:
            server_on = False
            print("Goodbye!")
        client.send(HTML_RESPONSE)
        client.close()
    sock.close()
