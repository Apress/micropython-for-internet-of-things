# MicroPython for the IOT - Chapter 10
#
# Project 3: MicroPython Plant Monitoring
#
# Plant monitor class
#
# Note: this only runs on the WiPy.
from machine import ADC, Pin, SD, Timer
import os
import utime

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
            sd = SD()
            os.mount(sd, '/sd')
            self.sensor_file = "/sd/{0}".format(SENSOR_DATA)
            print("INFO: Using SD card for data.")
        except:
            print("ERROR: cannot mount SD card, reverting to flash!")
            self.sensor_file = SENSOR_DATA
        print("Data filename = {0}".format(self.sensor_file))

        # Setup the dictionary for each soil moisture sensor
        adc = ADC(0)
        soil_moisture1 = {
            'sensor': adc.channel(pin='P13', attn=3),
            'power': Pin('P19', Pin.OUT),
            'location': 'Green ceramic pot on top shelf',
            'num': 1,
        }
        soil_moisture2 = {
            'sensor': adc.channel(pin='P14', attn=3),
            'power': Pin('P20', Pin.OUT),
            'location': 'Fern on bottom shelf',
            'num': 2,
        }
        # Setup a list for each sensor dictionary
        self.sensors = [soil_moisture1, soil_moisture2]
        # Setup the alarm to read the sensors
        a = Timer.Alarm(handler=self._read_sensors, s=UPDATE_FREQ,
                        periodic=True)
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
        power.value(1)
        for i in range (0,10):
            # Wait for sensor to power on and settle
            utime.sleep(5)
            # Read the value
            value = sensor.value()
            total += value
        # Turn sensor off
        power.value(0)
        return int(total/10)

    # Monitor the sensors, read the values and save them
    def _read_sensors(self, line):
        log_file = open(self.sensor_file, 'a')
        for sensor in self.sensors:
            # Read the data from the sensor and convert the value
            value = self._get_value(sensor['sensor'], sensor['power'])
            print("Value read: {0}".format(value))
            time_data = self.rtc.now()
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
