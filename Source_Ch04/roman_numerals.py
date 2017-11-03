#
# MicroPython for the IOT
# 
# Example: Roman numerals class
#
# Convert integers to roman numerals
# Convert roman numerals to integers
#
# Dr. Charles Bell
#

class Roman_Numerals:

    # Private dictionary of roman numerals
    __roman_dict = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000,
    }

    def convert_to_int(self, roman_num):
        value = 0
        for i in range(len(roman_num)):  
            if i > 0 and self.__roman_dict[roman_num[i]] > self.__roman_dict[roman_num[i - 1]]:  
                value += self.__roman_dict[roman_num[i]] - 2 * self.__roman_dict[roman_num[i - 1]]  
            else:  
                value += self.__roman_dict[roman_num[i]]
        return value
    
    def convert_to_roman(self, int_value):
        # First, get the values of all of entries in the dictionary
        roman_values = list(self.__roman_dict.values())
        roman_keys = list(self.__roman_dict.keys())
        # Prepare the string
        roman_str = ""
        remainder = int_value
        # Loop through the values in reverse
        for i in range(len(roman_values)-1, -1, -1):
            count = int(remainder / roman_values[i])
            if count > 0:
                for j in range(0,count):
                    roman_str += roman_keys[i]
                remainder -= count * roman_values[i]
        return roman_str
        
