# MicroPython for the IOT - Chapter 5
# Example use of the utime library
# Note: This example only works on the WiPy
# Note: This example will not on your PC.
import machine
import sys
import utime

# Since we don't have a RTC, we have to set the current time
# initialized the RTC in the WiPy machine library
from machine import RTC

# Init with default time and date
rtc = RTC()
# Init with a specific time and date. We use a specific
# datetime, but we could get this from a network time
# service.
rtc = RTC(datetime=(2017, 7, 15, 21, 32, 11, 0, None))

# Get a random number from 0-1 from a 2^24 bit random value
def get_rand():
    return machine.rng() / (2 ** 24 - 1)

# Format the time (epoch) for a better view
def format_time(tm_data):
    # Use a special shortcut to unpack tuple: *tm_data
    return "{0}-{1:0>2}-{2:0>2} {3:0>2}:{4:0>2}:{5:0>2}".format(*tm_data)

# Generate a random number of rows from 0-25
num_rows = get_rand() * 25

# Print a row using random seconds, milleseconds, or microseconds
# to simulate time.
print("Datetime             Value")
print("-------------------  --------")
for i in range(0,num_rows):
    # Generate random value for our sensor
    value = get_rand() * 100
    # Wait a random number of seconds for time
    utime.sleep(int(get_rand() * 15))  # sleep up to 15 seconds
    print("{0}  {1:0>{width}.4f}".format(format_time(rtc.now()), value, width=8))


