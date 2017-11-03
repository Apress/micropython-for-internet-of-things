# MicroPython for the IOT - Chapter 5
# Example use of exceptions
values = []
print("Start sensor read.")
try:
    values.append(read_sensor(pin11))
    values.append(read_sensor(pin12))
    values.append(read_sensor(pin13))
    values.append(read_sensor(pin17))
    values.append(read_sensor(pin18))
except ValueError as err:
    print("WARNING: One or more sensors valued to read a correct value.", err)
else:
    print("ERROR: fatal error reading sensors.")
finally:
    print("Sensor read complete.")
