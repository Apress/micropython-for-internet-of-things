# MicroPython for the IOT - Chapter 6
# Simple example for working with the SPI interface
# using the Adafruit Thermocouple Amplifier. See
# https://www.adafruit.com/product/269.
#
# Note: this only runs on the Pyboard
#
import machine
import ubinascii

# First, make sure this is running on a Pyboard
try:
    import pyb
    from pyb import SPI
except ImportError:
    print("ERROR: not on a Pyboard!")
    sys.exit(-1)

# Create a method to normalize the data into degrees Celsius
def normalize_data(data):
    temp = data[0] << 8 | data[1]
    if temp & 0x0001:
        return float('NaN')
    temp >>= 2
    if temp & 0x2000:
        temp -= 16384
    return (temp * 0.25)

# Setup the SPI interfaceon the "Y" interface
spi = SPI(2, SPI.MASTER, baudrate=5000000, polarity=0, phase=0)
cs = machine.Pin("Y5", machine.Pin.OUT)
cs.high()

# read from the chip
print("Reading temperature every second.")
print("Press CTRL-C to stop.")
while True:
    pyb.delay(1000)
    cs.low()
    print("Temperature is {0} Celsius.".format(normalize_data(spi.recv(4))))
    cs.high()


