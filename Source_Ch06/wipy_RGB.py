# MicroPython for the IOT - Chapter 6
# Example of using the I2C interface via a driver
# for the Adafruit RGB Sensor tcs34725
#
# Requires library:
# https://github.com/adafruit/micropython-adafruit-tcs34725
#
from machine import I2C, Pin
import sys
import tcs34725
import utime

# Method to read sensor and display results
def read_sensor(rgb_sense, led):
    sys.stdout.write("Place object in front of sensor now...")
    led.value(1)                 # Turn on the LED
    utime.sleep(5)               # Wait 5 seconds
    data = rgb_sense.read(True)  # Get the RGBC values
    print("color detected: {")
    print("    Red: {0:03}".format(data[0]))
    print("  Green: {0:03}".format(data[1]))
    print("   Blue: {0:03}".format(data[2]))
    print("  Clear: {0:03}".format(data[3]))
    print("}")
    led.value(0)

# Setup the I2C - easy, yes?
i2c = I2C(0, I2C.MASTER)             # create and init as a master
i2c.init(I2C.MASTER, baudrate=20000) # init as a master
i2c.scan()

# Setup the sensor
sensor = tcs34725.TCS34725(i2c)

# Setup the LED pin
led_pin = Pin("P8", Pin.OUT)
led_pin.value(0)

print("Reading Colors every 10 seconds. When LED is on, place object in front of sensor.")
print("Press CTRL-C to quit. (wait for it)")
while True:
    utime.sleep(10)               # Sleep for 10 seconds
    read_sensor(sensor, led_pin)  # Read sensor and display values
    
    

