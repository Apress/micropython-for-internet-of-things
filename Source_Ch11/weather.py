# MicroPython for the IOT - Chapter 11
#
# Project 4: MicroPython Weather Node
#
# Required Components:
# - WiPy
# - (1) BME280 Weather Sensor
#
# Note: this only runs on the WiPy.
#
# Imports for the project
from network import WLAN
from weather_node import WeatherNode
import machine

# Define out user id and key
_IO_ID = "YOUR_DEVICE_ID"
_IO_USERNAME ="YOUR_USER_ID"
_IO_KEY = "YOUR_AIO_KEY"
_FREQUENCY = 5 # seconds

# Setup the board to connect to our network.
def connect():
    wlan = WLAN(mode=WLAN.STA)
    nets = wlan.scan()
    for net in nets:
        if net.ssid == 'YOUR_SSID':
            print('Network found!')
            wlan.connect(net.ssid, auth=(net.sec, 'YOUR_SSID_PASSWORD'), timeout=5000)
            while not wlan.isconnected():
                machine.idle() # save power while waiting
            print('WLAN connection succeeded!')
            print("My IP address is: {0}".format(wlan.ifconfig()[0]))
            return True
    return False

def run():
    # Setup our Internet connection
    connect()

    # Run the weather MQTT client
    weather_mqtt_client = WeatherNode(_IO_ID, _IO_USERNAME, _IO_KEY, _FREQUENCY)
    weather_mqtt_client.run()
