# MicroPython for the IOT - Chapter 10
#
# Project 3: MicroPython Plant Monitoring
#
# Plant monitor class
#
# Note: this only runs on the Pyboard.
from pyb import ADC, delay, Pin, SD
import os
import pyb

# Thresholds for the sensors
LOWER_THRESHOLD = 500
UPPER_THRESHOLD = 2500
UPDATE_FREQ = 120   # seconds

# File name for the data
SENSOR_DATA = "plant_data.csv"

# Format the time (epoch) for a better view
def _format_time(tm_data):
    # Use a special shortcut to unpack tuple: *tm_data
    return "{0}-{1:0>2}-{2:0>2} {3:0>2}:{4:0>2}:{5:0>2}".format(*tm_data)

class PlantMonitor:
    """
    This class reads soil moisture from one or more sensors and writes the
    data to a comma-separated value (csv) file as specified in the constructor.
    """

    # Initialization for the class (the constructor)
    def __init__(self, rtc):
        self.rtc = rtc

        # Try to access the SD card and make the new path
        try:
            self.sensor_file = "/sd/{0}".format(filename)
            f = open(self.sensor_file, 'r')
            f.close()
            print("INFO: Using SD card for data.")
        except:
            print("ERROR: cannot mount SD card, reverting to flash!")
            self.sensor_file = SENSOR_DATA
        print("Data filename = {0}".format(self.sensor_file))

        # Setup the dictionary for each soil moisture sensor
        soil_moisture1 = {
            'sensor': ADC(Pin('X19')),
            'power': Pin('X20', Pin.OUT_PP),
            'location': 'Green ceramic pot on top shelf',
            'num': 1,
        }
        soil_moisture2 = {
            'sensor': ADC(Pin('X20')),
            'power': Pin('X21', Pin.OUT_PP),
            'location': 'Fern on bottom shelf',
            'num': 2,
        }
        # Setup a list for each sensor dictionary
        self.sensors = [soil_moisture1, soil_moisture2]
        # Setup the alarm to read the sensors
        self.alarm = pyb.millis()
        print("Plant Monitor class is ready...")

    # Clear the log
    def clear_log(self):
        log_file = open(self.sensor_file, 'w')
        log_file.close()

    # Get the filename we're using after the check for SD card
    def get_filename(self):
        return self.sensor_file

    # Read the sensor 10 times and average the values read
    def _get_value(self, sensor, power):
        total = 0
        # Turn power on
        power.high()
        for i in range (0,10):
            # Wait for sensor to power on and settle
            delay(5000)
            # Read the value
            value = sensor.read()
            total += value
        # Turn sensor off
        power.low()
        return int(total/10)

    # Monitor the sensors, read the values and save them
    def read_sensors(self):
        if pyb.elapsed_millis(self.alarm) < (UPDATE_FREQ * 1000):
            return
        self.alarm = pyb.millis()
        log_file = open(self.sensor_file, 'a')
        for sensor in self.sensors:
            # Read the data from the sensor and convert the value
            value = self._get_value(sensor['sensor'], sensor['power'])
            print("Value read: {0}".format(value))
            time_data = self.rtc.datetime()
            # datetime,num,value,enum,location
            log_file.write(
                "{0},{1},{2},{3},{4}\n".format(_format_time(time_data),
                                               sensor['num'], value,
                                               self._convert_value(value),
                                               sensor['location']))
        log_file.close()

    # Convert the raw sensor value to an enumeration
    def _convert_value(self, value):
        # If value is less than lower threshold, soil is dry else if it
        # is greater than upper threshold, it is wet, else all is well.
        if (value <= LOWER_THRESHOLD):
            return "dry"
        elif (value >= UPPER_THRESHOLD):
            return "wet"
        return "ok"
