#
# MicroPython for the IOT
# 
# Example: Fibonacci series using recursion
#
# Calculate the Fibonacci series based on user input
#
# Dr. Charles Bell
#

# Create a function to calculate Fibonacci series (iterative)
# Returns a list.
def fibonacci_iterative(count):
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib

# Create a function to calculate the nth Fibonacci number (recursive)
# Returns an integer.
def fibonacci_recursive(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        # Call our self counting down.
        value = fibonacci_recursive(number-1) + fibonacci_recursive(number-2)
        return value
    
# Main code
print("Welcome to my Fibonacci calculator!")
index = int(input("Please enter the number of integers in the series: "))

# Recursive example
print("We calculate the value using a recursive algoritm.")
nth_fibonacci = fibonacci_recursive(index)
print("The {0}{1} fibonacci number is {2}."
      "".format(index, "th" if index > 1 else "st", nth_fibonacci))
see_series = str(input("Do you want to see all of the values in the series? "))
if see_series in ["Y","y"]:
    series = []
    for i in range(1,index+1):
        series.append(fibonacci_recursive(i))
    print("Series: {0}: ".format(series))

# Iterative example
print("We calculate the value using an iterative algoritm.")
series = fibonacci_iterative(index)
print("The {0}{1} fibonacci number is {2}."
      "".format(index, "th" if index > 1 else "st", series[index-1]))
see_series = str(input("Do you want to see all of the values in the series? "))
if see_series in ["Y","y"]:
    print("Series: {0}: ".format(series))
print("bye!")
