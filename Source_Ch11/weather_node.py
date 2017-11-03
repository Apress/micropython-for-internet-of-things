# MicroPython for the IOT - Chapter 11
#
# Project 4: MicroPython Weather Node - BME280 MQTT Client class
#
# Note: this only runs on the WiPy.
#
# Imports for the project
from machine import I2C
from mqtt import MQTTClient
import bme280
import utime

class WeatherNode:
    """Sensor node using a BME280 sensor to send temperature, humidity, and
       barometric pressure to io.adafruit.com MQTT broker."""

    # Constructor
    def __init__(self, io_id, io_user, io_key, frequency, port=1883):
        # Turn sensors on/off
        self.sensor_on = False

        # Save variables passed for use in other methods
        self.io_id = io_id
        self.io_user = io_user
        self.io_key = io_key
        self.update_frequency = frequency
        self.port = port

        # Now, setup the sensor
        i2c = I2C(0, I2C.MASTER, baudrate=100000)
        self.sensor = bme280.BME280(i2c=i2c)
        utime.sleep_ms(100)
        print("Weather MQTT client is ready.")

    # Reads the sensor. Returns a tuple of (temperature, humidity, pressure)
    def read_data(self):
        utime.sleep_ms(50)
        temperature = self.sensor.read_temperature() / 100.00
        humidity = self.sensor.read_humidity() / 1024.00
        pressure = self.sensor.read_pressure() / 256.00
        return (temperature, humidity, pressure)

    # A test to read data from a file and publish it.
    def read_data_test(self, client):
        data_file = open("weather.csv", "r")
        for row in data_file:
            data = row.strip("\n").split(",")
            print(" >", data)
            client.publish(topic="{0}/feeds/temperature".format(self.io_user),
                           msg=str(data[0]))
            client.publish(topic="{0}/feeds/humidity".format(self.io_user),
                           msg=str(data[1]))
            client.publish(topic="{0}/feeds/pressure".format(self.io_user),
                           msg=str(data[2]))
            utime.sleep(self.update_frequency)
        data_file.close()

    # A simple callback to print the message from the server
    def message_callback(self, topic, msg):
        print("[{0}]: {1}".format(topic, msg))
        self.sensor_on = (msg == b'ON')

    def run(self):
        # Now we setup our MQTT client
        client = MQTTClient(self.io_id, "io.adafruit.com", user=self.io_user,
                            password=self.io_key, port=self.port)
        client.set_callback(self.message_callback)
        client.connect()
        client.subscribe(topic="{0}/feeds/sensors".format(self.io_user))

        while True:
            if self.sensor_on:
                data = self.read_data()
                print(" >", data)
                client.publish(topic="{0}/feeds/temperature".format(self.io_user),
                               msg=str(data[0]))
                client.publish(topic="{0}/feeds/humidity".format(self.io_user),
                               msg=str(data[1]))
                client.publish(topic="{0}/feeds/pressure".format(self.io_user),
                               msg=str(data[2]))
                utime.sleep(self.update_frequency)
            client.check_msg()
            utime.sleep(1)     # Check messages only once per second
