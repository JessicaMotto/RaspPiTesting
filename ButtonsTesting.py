import RPi.GPIO as GPIO
import time
import AdaFruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Input pins:
L_pin = 27
R_pin = 23
C_pin = 17
U_pin = 13
D_pin = 16
A_pin = 25
B_pin = 12
LED_pin = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(A_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(B_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(L_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(R_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
CGPIO.setup(U_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(D_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(C_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(26, GPIO.OUT)

# Raspberry Pi pin configuration:
RST = 24

# 128x32 display wih hardware I2C:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library
disp.begin()

# Clear library
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image
draw = ImageDraw(image)

# Draw a black filled box to clear the image/
draw.rectangle((0, 0, width, height), outline0, fill=0)


try:
  while 1:
    if GPIO.input(U_pin): # button is released
      draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=0)  # Up
    else: # button is pressed:
      draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=1)  # Up filled
    if GPIO.input(L_pin): # button is released
      draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0)  # Left
    else: # button is pressed:
      draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=1)  # Left filled
    if GPIO.input(R_pin): # button is released
      draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=0) # Right
    else: # button is pressed:
      draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=1) # Right filled
    if GPIO.input(D_pin): # button is released
      draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=0) # Down
      GPIO.output(26, GPIO.LOW)
    else: # button is pressed:
      draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=1) # Down filled
      GPIO.output(26, GPIO.HIGH)
    if GPIO.input(C_pin): # button is released
      draw.rectangle((20, 22,40,40), outline=255, fill=0) # Center
    else: # button is pressed:
      draw.rectangle((20, 22,40,40), outline=255, fill=1) # Center filled
    if GPIO.input(A_pin): # button is released
      draw.ellipse((70,40,90,60), outline=255, fill=0) # A button
    else: # button is pressed:
      draw.ellipse((70,40,90,60), outline=255, fill=1) # A button filled
    if GPIO.input(B_pin): # button is released
      draw.ellipse((100,20,120,40), outline=255, fill=0) # B button
    else: # button is pressed:
      draw.ellipse((100, 20, 120, 40), outline=255, fill=1) # B button filled
    if not GPIO.input(A_pin) and not GPIO.input(B_pin) and not GPIO.input(C$
      catImage = Image.open('happycat_oled_64.ppm').convert('1')
      disp.image(catImage)
    else:
      # Display image.
        disp.image(image)
    disp.display()
    time.sleep(0.01)
    
    
except KeyboardInterrupt:
  GPIO.cleanup()
