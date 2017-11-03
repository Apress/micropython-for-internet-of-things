# MicroPython for the IOT - Chapter 9
#
# Project 2: A MicroPython Pedestrian Crosswalk Simulator
#            Part 3 - controlling LEDs over the Internet
#
# Required Components:
# - WiPy
# - (2) Red LEDs
# - (2) Yellow LEDs
# - (1) Green LED
# - (5) 220 Ohm resistors
#
# Note: this only runs on the WiPy.
#
# Imports for the project
from machine import Pin
import usocket as socket
import utime
import machine
from network import WLAN

# Setup the board to connect to our network.
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
for net in nets:
    if net.ssid == 'YOUR_SSID':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'YOUR_PASSWORD'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        print("My IP address is: {0}".format(wlan.ifconfig()[0]))
        break

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

# Setup the LEDs (button no longer needed)
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
