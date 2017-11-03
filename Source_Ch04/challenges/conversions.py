#
# MicroPython for the IOT
# 
# Challenge Example: Convert integer to binary, hex, and octal 
#
# Dr. Charles Bell
#
import argparse
# Setup the argument parser
parser = argparse.ArgumentParser()
# We need two arguments: integer, and conversion
parser.add_argument("original_val", help="Value to convert.")
parser.add_argument("conversion", help="Conversion: hex, bin, or oct.")
# Get the arguments
args = parser.parse_args()
# Convert string to integer
value = int(args.original_val)
if args.conversion == 'bin':
    print("{0} in binary is {1}".format(value, bin(value)))
elif args.conversion == 'oct':
    print("{0} in octal is {1}".format(value, oct(value)))
elif args.conversion == 'hex':
    print("{0} in hexadecimal is {1}".format(value, hex(value)))
else:
    print("Sorry, I don't understand, {0}.".format(args.conversion))
