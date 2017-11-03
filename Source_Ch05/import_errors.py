# MicroPython for the IOT - Chapter 5
# Try to import the keys() function from piano
try:
    from piano import keys
except ImportError as err:
    print("WARNING:", err)
    def keys():
        return(['A','B','C','D','E','F','G'])

print("Keys:", keys())
