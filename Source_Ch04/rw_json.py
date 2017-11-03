#
# MicroPython for the IOT
# 
# Example: Storing and retrieving JSON objects in files
#
# Dr. Charles Bell
#

import json

# Prepare a list of JSON documents for pets by converting JSON to a dictionary
pets = []
parsed_json = json.loads('{"name":"Violet", "age": 6, "breed":"dachshund", "type":"dog"}')
pets.append(parsed_json)
parsed_json = json.loads('{"name": "JonJon", "age": 15, "breed":"poodle", "type":"dog"}')
pets.append(parsed_json)
parsed_json = json.loads('{"name": "Mister", "age": 4, "breed":"siberian khatru", "type":"cat"}')
pets.append(parsed_json)
parsed_json = json.loads('{"name": "Spot", "age": 7, "breed":"koi", "type":"fish"}')
pets.append(parsed_json)
parsed_json = json.loads('{"name": "Charlie", "age": 6, "breed":"dachshund", "type":"dog"}')
pets.append(parsed_json)

# Now, write these entries to a file. Note: overwrites the file
json_file = open("my_data.json", "w")
for pet in pets:
    json_file.write(json.dumps(pet))
    json_file.write("\n")
json_file.close()

# Now, let's read the JSON documents then print the name and age for all of the dogs in the list
my_pets = []
json_file = open("my_data.json", "r")
for pet in json_file.readlines():
    parsed_json = json.loads(pet)
    my_pets.append(parsed_json)
json_file.close()

print("Name, Age")
for pet in my_pets:
    if pet['type'] == 'dog':
        print("{0}, {1}".format(pet['name'], pet['age']))


