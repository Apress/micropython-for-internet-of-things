# MicroPython for the IOT - Chapter 8
#
# Project 1: A MicroPython Clock!
#
# Required Components:
# - Pyboard
# - OLED SPI display
# - RTC I2C module
#
# Note: this only runs on the WiPy. See chapter text
#       for how to modify this to run on the Pyboard.
#

# Imports for the project
import urtc
import utime
from machine import SPI, I2C, RTC as rtc, Pin as pin
from ssd1306 import SSD1306_SPI as ssd

# Setup SPI and I2C 
spi = SPI(0, SPI.MASTER, baudrate=2000000, polarity=0, phase=0)
i2c = I2C(0, I2C.MASTER, baudrate=100000,pins=("P9", "P8"))

# Setup the OLED : D/C, RST, CS
oled_module = ssd(128,32,spi,pin('P5'),pin('P6'),pin('P7'))

# Setup the RTC
rtc_module = urtc.DS1307(i2c)
#
# NOTE: We only need to set the datetime once. Uncomment these
#       lines only on the first run of a new RTC module or
#       whenever you change the battery.
#       (year, month, day, weekday, hour, minute, second, millisecond)
#start_datetime = (2017,07,20,4,9,0,0,0)
#rtc_module.datetime(start_datetime)

# Return a string to print the day of the week
def get_weekday(day):
    if day == 1: return "Sunday"
    elif day == 2: return "Monday"
    elif day == 3: return "Tuesday"
    elif day == 4: return "Wednesday"
    elif day == 5: return "Thursday"
    elif day == 6: return "Friday"
    else: return "Saturday"

# Display the date and time
def write_time(oled, rtc):
    # Get datetime
    dt = rtc.datetime()
    # Print the date
    oled.text("Date: {0:02}/{1:02}/{2:04}".format(dt[1], dt[2], dt[0]), 0, 0)
    # Print the time
    oled.text("Time: {0:02}:{1:02}:{2:02}".format(dt[4], dt[5], dt[6]), 0, 10)
    # Print the day of the week
    oled.text("Day:  {0}".format(get_weekday(dt[3])), 0, 20)
    # Update the OLED
    oled.show()

# Clear the screen
def clear_screen(oled):
    oled.fill(0)
    oled.show()
    
# Here, we make a "run" function to be used from the main.py
# code module. This is preferable to direct "main" execution.
def run():
    # Display the deate and time every second
    while True:
        clear_screen(oled_module)
        write_time(oled_module, rtc_module)
        utime.sleep(1)
