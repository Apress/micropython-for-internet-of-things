import urtc
from pyb import I2C
from machine import Pin as pin
i2c = I2C(1, I2C.MASTER)
i2c.init(I2C.MASTER, baudrate=500000)
i2c.scan()
rtc = urtc.DS1307(i2c)
# year, month, day, weekday, hour, minute, second, millisecond)
start_datetime = (2017,07,20,4,7,25,0,0)
rtc.datetime(start_datetime)
print(rtc.datetime())
