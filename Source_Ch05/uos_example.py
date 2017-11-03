# MicroPython for the IOT - Chapter 5
# Example use of the uos library
# Note: change uos to os to run it on your PC!
import sys
import uos

# Create a method to display files in directory
def show_files():
    files = uos.listdir()
    sys.stdout.write("\nShow Files Output:\n")
    sys.stdout.write("\tname\tsize\n")
    for file in files:
        stats = uos.stat(file)
        # Print a directory with a "d" prefix and the size
        is_dir = True
        if stats[0] > 16384:
            is_dir = False
        if is_dir:
            sys.stdout.write("d\t")
        else:
            sys.stdout.write("\t")
        sys.stdout.write(file)
        if not is_dir:
            sys.stdout.write("\t")
            sys.stdout.write(str(stats[6]))
        sys.stdout.write("\n")

# List the current directory
show_files()
# Change to the examples directory
uos.chdir('examples')
show_files()

# Show how you can now use the import statement with the current dir
print("\nRun the ujson_example with import ujson_example after chdir()")
import ujson_example

# Create a directory
uos.mkdir("test")
show_files()

# Remove the directory
uos.rmdir('test')
show_files()
