# MicroPython for the IOT - Chapter 5
# Example use of the uio library
# Note: change uio to io to run this on your PC!
import uio
# Create the binary file
fio_out = uio.FileIO('data.bin', 'wb')
fio_out.write("\x5F\x9E\xAE\x09\x3E\x96\x68\x65\x6C\x6C\x6F")
fio_out.write("\x00")
fio_out.close()
# Read the binary file and print out the results in hex and char.
fio_in = uio.FileIO('data.bin', 'rb')
print("Raw,Dec,Hex from file:")
byte_val = fio_in.read(1)  # read a byte
while byte_val:
    print(byte_val, ",", ord(byte_val), hex(ord(byte_val)))
    byte_val = fio_in.read(1)  # read a byte
fio_in.close()

