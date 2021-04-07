import time
import board
import busio
from time import strftime, sleep
import adafruit_mpr121
import digitalio
from PIL import Image, ImageDraw, ImageFont

from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
import webcolors

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

# set up screen display

# The display uses a communication protocol called SPI.
# SPI will not be covered in depth in this course.
# you can read more https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # the rate  the screen talks to the pi
# Create the ST7789 display:
buttonPin = 18
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

disp = st7789.ST7789(
    board.SPI(),
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
    rotation = 90
)
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.height  # we swap height/width to rotate it to landscape!
    height = disp.width

image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
x = 20
y = height //2 -30
draw.text((x,y), "Don't touch my cookie! ", font=font, fill=(255, 0, 0))
disp.image(image)


while True:
    for i in range(12):
        if mpr121[i].value:
            print("stolen!")
            text = "Someone stole the cookie\n from the cookie jar\n at" + strftime("%m/%d/%Y %H:%M:%S")
            image = Image.new("RGB", (width, height))
            draw = ImageDraw.Draw(image)
            draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
            x = 10
            y = height //2 -30
            draw.text((x,y), text, font=font, fill=(255, 0, 0))
            disp.image(image)

    time.sleep(0.1)  # Small delay to keep from spamming output messages.
