#from https://github.com/MonomCZ/MeowPi-3
from PIL import Image, ImageDraw
import board
import busio
import adafruit_ssd1306
import subprocess


WIDTH = 128
HEIGHT = 64

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)
oled.show()

image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

# the display fits 21 character per line

def display_text(text,y):
# ^ means next line
    
    text.split("^")
    for i in range(len(text.split("^"))):
        draw.text((0, y + (i*10)), text.split("^")[i], fill=255)

    str.replace(text, "^", "")



def clear():
    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0) 


def display_temperature():
    output = subprocess.check_output(["vcgencmd", "measure_temp"]).decode().strip()
    output = str.replace(output, "temp=", "                                                ")
    output = str.replace(output, "'", "°")
    display_text(output, 20)

def show():
    oled.image(image)
    oled.show()