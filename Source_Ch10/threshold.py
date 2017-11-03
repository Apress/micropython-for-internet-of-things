# MicroPython for the IOT - Chapter 10
#
# Project 3: MicroPython Plant Monitoring
#
# Threshold calibration for soil moisture sensors
#
# Note: this only runs on the WiPy.
from machine import ADC, Pin
import utime

# Setup the ADC channel for the read (signal)
# Here we choose pin P13 and set attn to 3 to stabilize voltage
adc = ADC(0)
sensor = adc.channel(pin='P13', attn=3)

# Setup the GPIO pin for powering the sensor. We use Pin 19
power = Pin('P19', Pin.OUT)
# Turn sensor off
power.value(0)

# Loop 10 times and average the values read
print("Reading 10 values.")
total = 0
for i in range (0,10):
    # Turn power on
    power.value(1)
    # Wait for sensor to power on and settle
    utime.sleep(5)
    # Read the value
    value = sensor.value()
    print("Value read: {0}".format(value))
    total += value
    # Turn sensor off
    power.value(0)
    
# Now average the values
print("The average value read is: {0}".format(total/10))

    
