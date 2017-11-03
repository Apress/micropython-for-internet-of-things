# Example code to demonstrate writing and reading data to/from files

# Step 1: Create a file and write some data
new_file = open("log.txt", "w")    # use "write" mode
new_file.write("1,apples,2.5\n")   # write some data
new_file.write("2,oranges,1\n")    # write some data
new_file.write("3,peaches,3\n")    # write some data
new_file.write("4,grapes,21\n")    # write some data
new_file.close()  # close the file

# Step 2: Open a file and read data
old_file = open("log.txt", "r")  # use "read" mode
# Use a loop to read all rows in the file
for row in old_file.readlines():
    columns = row.strip("\n").split(",") # split row by commas
    print(" : ".join(columns))  # print the row with colon separator
old_file.close()
