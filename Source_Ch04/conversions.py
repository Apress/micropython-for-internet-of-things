#
# MicroPython for the IOT
# 
# Example: Convert integer to binary, hex, and octal
#
# Dr. Charles Bell
#

# Create a tuple of integer values
values = (12, 450, 1, 89, 2017, 90125)

# Loop through the values and convert each to binary, hex, and octal
for value in values:
    print("{0} in binary is {1}".format(value, bin(value)))
    print("{0} in octal is {1}".format(value, oct(value)))
    print("{0} in hexadecimal is {1}".format(value, hex(value)))

