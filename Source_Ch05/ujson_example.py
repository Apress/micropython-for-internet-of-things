# MicroPython for the IOT - Chapter 5
# Example use of the ujson library
# Note: change ujson to json to run it on your PC!
import ujson

# Prepare a list of JSON documents for pets by converting JSON to a dictionary
vehicles = []
vehicles.append(ujson.loads('{"make":"Chevrolet", "year":2015, "model":"Silverado", "color":"Pull me over red", "type":"pickup"}'))
vehicles.append(ujson.loads('{"make":"Yamaha", "year":2009, "model":"R1", "color":"Blue/Silver", "type":"motorcycle"}'))
vehicles.append(ujson.loads('{"make":"SeaDoo", "year":1997, "model":"Speedster", "color":"White", "type":"boat"}'))
vehicles.append(ujson.loads('{"make":"TaoJen", "year":2013, "model":"Sicily", "color":"Black", "type":"Scooter"}'))

# Now, write these entries to a file. Note: overwrites the file
json_file = open("my_vehicles.json", "w")
for vehicle in vehicles:
    json_file.write(ujson.dumps(vehicle))
    json_file.write("\n")
json_file.close()

# Now, let's read the list of vehicles and print out their data
my_vehicles = []
json_file = open("my_vehicles.json", "r")
for vehicle in json_file.readlines():
    parsed_json = ujson.loads(vehicle)
    my_vehicles.append(parsed_json)
json_file.close()

# Finally, print a summary of the vehicles
print("Year Make Model Color")
for vehicle in my_vehicles:
    print(vehicle['year'],vehicle['make'],vehicle['model'],vehicle['color'])

