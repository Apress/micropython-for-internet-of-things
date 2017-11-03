# MicroPython for the IOT - Chapter 6
# Simple example for working with encrypting data
#
import sys

# First, make sure this is running on a WiPy (pycom)
try:
    import pycom
    from crypto import AES
except ImportError:
    print("ERROR: not on a WiPy (or Pycom) board!")
    sys.exit(-1)

# Setup encryption using simple, basic encryption
# NOTICE: you normally would protect this key!
my_key = b'monkeybreadyummy' # 128 bit (16 bytes) key
cipher = AES(my_key, AES.MODE_ECB)

# Create the file and encrypt the data
new_file = open("secret_log.txt", "w")    # use "write" mode
new_file.write(cipher.encrypt("1,apples,2.5   \n"))   # write some data
new_file.write(cipher.encrypt("2,oranges,1    \n"))    # write some data
new_file.write(cipher.encrypt("3,peaches,3    \n"))    # write some data
new_file.write(cipher.encrypt("4,grapes,21    \n"))    # write some data
new_file.close()  # close the file

# Step 2: Open the file and read data 
old_file = open("secret_log.txt", "r")  # use "read" mode
# Use a loop to read all rows in the file
for row in old_file.readlines():
    data = cipher.decrypt(row).decode('ascii')
    columns = data.strip("\n").split(",") # split row by commas
    print(" : ".join(columns))  # print the row with colon separator
    
old_file.close()
