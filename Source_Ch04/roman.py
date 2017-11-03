#
# MicroPython for the IOT
# 
# Example: Convert roman numerals using a class
#
# Convert integers to roman numerals
# Convert roman numerals to integers
#
# Dr. Charles Bell
#

from roman_numerals import Roman_Numerals

roman_str = input("Enter a valid roman numeral: ")
roman_num = Roman_Numerals()

# Convert to roman numberals
value = roman_num.convert_to_int(roman_str)
print("Convert to integer:        {0} = {1}".format(roman_str, value))

# Convert to integer
new_str = roman_num.convert_to_roman(value)
print("Convert to Roman Numerals: {0} = {1}".format(value, new_str))

print("bye!")
