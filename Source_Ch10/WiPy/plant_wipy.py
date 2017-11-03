# MicroPython for the IOT - Chapter 10
#
# Project 3: MicroPython Plant Monitoring
#
# Required Components:
# - WiPy
# - (N) Soil moisture sensors (one for each plant)
#
# Note: this only runs on the WiPy.
#
# Imports for the project
from machine import RTC
import sys
import usocket as socket
import utime
import machine
from network import WLAN
from plant_monitor import PlantMonitor

# HTML web page for the project
HTML_TABLE_ROW = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td></tr>"

# Setup the board to connect to our network.
def connect():
    wlan = WLAN(mode=WLAN.STA)
    nets = wlan.scan()
    for net in nets:
        if net.ssid == 'YOUR_SSID':
            print('Network found!')
            wlan.connect(net.ssid, auth=(net.sec, 'YOUR_PASSWORD'), timeout=5000)
            while not wlan.isconnected():
                machine.idle() # save power while waiting
            print('WLAN connection succeeded!')
            print("My IP address is: {0}".format(wlan.ifconfig()[0]))
            return True
    return False

# Setup the real time clock with the NTP service
def get_ntp():
    rtc = RTC()
    print("Time before sync:", rtc.now())
    rtc.ntp_sync("pool.ntp.org")
    while not rtc.synced():
        utime.sleep(3)
        print("Waiting for NTP server...")
    print("Time after sync:", rtc.now())
    return rtc

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
    log_file.close()
    send_html_file("part2.html", client)

# Setup the socket and respond to HTML requests
def run():
    # Connect to the network
    if not connect():
        sys.exit(-1)

    # Setup the real time clock
    rtc = get_ntp()

    # Setup the plant monitoring object instance from the plant_monitoring class
    plants = PlantMonitor(rtc)
    filename = plants.get_filename()

    # Setup the HTML server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 80))
    sock.listen(5)
    print("Ready for connections...")
    server_on = True
    while server_on:
        client, address = sock.accept()
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
