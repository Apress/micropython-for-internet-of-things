# MicroPython for the IOT - Chapter 6
# Example for working with the hearbeat LED as a
# status/state indicator
#
import utime

# First, make sure this is running on a Pyboard
try:
    import pycom
except ImportError:
    print("ERROR: not on a WiPy (or Pycom) board!")
    sys.exit(-1)
    
# State/status enumeration
_STATES = {
    'ERROR'   : 0xFF0000, # Bright red
    'READING' : 0x00FF00, # Green
    'WRITING' : 0x0000FF, # Blue
    'OK'      : 0xFF33FF, # Pinkish
}

# Clear the state (return to normal operation)
def clear_status():
    pycom.heartbeat(True)

# Show state/status with the heatbeat LED
def show_status(state):
    pycom.heartbeat(False)
    pycom.rgbled(state)
    
# Now, demonstrate the state changes
for state in _STATES.keys():
    show_status(_STATES[state])
    utime.sleep(3)
    
# Return heartbeat to normal
clear_status()
