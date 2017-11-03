import machine
from machine import Pin as pin
from ssd1306 import SSD1306_SPI as ssd
spi = machine.SPI(2, baudrate=8000000, polarity=0, phase=0)
oled = ssd(128,32,spi,pin("Y4"),pin("Y3"),pin("Y5"))
oled.fill(0)
oled.show()
oled.fill(1)
oled.show()
oled.fill(0)
oled.show()
oled.text("Hello, World!", 0, 0)
oled.show()
