# MicroPython for the IOT - Chapter 5
# Example use of the sys library
import sys
print("Modules loaded: " , sys.modules)
sys.path.append("/sd")
print("Path: ", sys.path)
sys.stdout.write("Platform: ")
sys.stdout.write(sys.platform)
sys.stdout.write("\n")
sys.stdout.write("Version: ")
sys.stdout.write(sys.version)
sys.stdout.write("\n")
sys.exit(1)
