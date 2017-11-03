# MicroPython for the IOT - Chapter 10
#
# Project 3: MicroPython Plant Monitoring
#
# Required Components:
# - Pyboard
# - (N) Soil moisture sensors (one for each plant)
#
# Note: this only runs on the Pyboard.
#
# Imports for the project
from pyb import delay, SPI
from pyb import I2C
import network
import urtc
import usocket as socket
from plant_monitor import PlantMonitor

# Setup the I2C interface for the rtc
i2c = I2C(1, I2C.MASTER)
i2c.init(I2C.MASTER, baudrate=500000)

# HTML web page for the project
HTML_TABLE_ROW = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td></tr>"

# Setup the board to connect to our network.
def connect():
    nic = network.CC3K(SPI(2), Pin.board.Y5, Pin.board.Y4, Pin.board.Y3)
    # Replace the following with yout SSID and password
    print("Connecting...")
    nic.connect("YOUR_SSID", "YOUR_PASSWORD")
    while not nic.isconnected():
        delay(50)
    print("Connected!")
    print("My IP address is: {0}".format(nic.ifconfig()[0]))
    return True

# Read HTML from file and send to client a row at a time.
def send_html_file(filename, client):
    html = open(filename, 'r')
    for row in html:
        client.send(row)
    html.close()

# Send the sensor data to the client.
def send_sensor_data(client, filename):
    send_html_file("part1.html", client)
    log_file = open(filename, 'r')
    for row in log_file:
        cols = row.strip("\n").split(",") # split row by commas
        # build the table string if all parts are there
        if len(cols) >= 5:
            html = HTML_TABLE_ROW.format(cols[0], cols[1], cols[2],
                                         cols[3], cols[4])
            # send the row to the client
            client.send(html)
            delay(50)
    log_file.close()
    send_html_file("part2.html", client)

# Setup the socket and respond to HTML requests
def run():
    # Connect to the network
    if not connect():
        sys.exit(-1)

    # Setup the real time clock
    rtc = urtc.DS1307(i2c)
    #
    # NOTE: We only need to set the datetime once. Uncomment these
    #       lines only on the first run of a new RTC module or
    #       whenever you change the battery.
    #       (year, month, day, weekday, hour, minute, second, millisecond)
    #start_datetime = (2017,07,20,4,9,0,0,0)
    #rtc.datetime(start_datetime)

    # Setup the plant monitoring object instance from the plant_monitoring class
    plants = PlantMonitor(rtc)
    filename = plants.get_filename()

    # Setup the HTML server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 80))
    sock.setblocking(False)   # We must use polling for Pyboard.
    sock.listen(5)
    print("Ready for connections...")
    server_on = True
    while server_on:
        try:
            client, address = sock.accept()
        except OSError as err:
            # Do check for reading sensors here
            plants.read_sensors()
            delay(50)
            continue
        print("Got a connection from a client at: %s" % str(address))
        request = client.recv(1024)

        # Allow for clearing of the log, but be careful! The auto refresh
        # will resend this command if you do not clear it from your URL
        # line.

        if (request[:14] == b'GET /CLEAR_LOG'):
            print('Requesting clear log.')
            plants.clear_log()
        send_sensor_data(client, filename)
        client.close()
    sock.close()
