# MicroPython for the IOT - Chapter 5
# Example module for using the ntptime server to set the datetime
# Note: only works on WiPy!

from network import WLAN
from machine import RTC
import machine
import sys
import utime

wlan = WLAN(mode=WLAN.STA)

def connect():
    wifi_networks = wlan.scan()
    for wifi in wifi_networks:
        if wifi.ssid == "YOUR_SSID":
            wlan.connect(wifi.ssid, auth=(wifi.sec, "YOUR_SSID_PASSWORD"), timeout=5000)
            while not wlan.isconnected():
                machine.idle() # save power while waiting
            print("Connected!")
            return True
    if not wlan.isconnected():
        print("ERROR: Cannot connect! Exiting...")
        return False

if not connect():
    sys.exit(-1)

# Now, setup the RTC with the NTP service.
rtc = RTC()
print("Time before sync:", rtc.now())
rtc.ntp_sync("pool.ntp.org")
while not rtc.synced():
    utime.sleep(1)
    print("waiting for NTP server...")
print("Time after sync:", rtc.now())

