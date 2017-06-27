import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LED1 = 17
LED2 = 23
PIR_pin = 26

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(PIR_pin, GPIO.IN)

def LIGHTS(PIR_pin):
  #Turns LEDS On and OFF
  print('Motion Detected!')
  print('Lights on')
  GPIO.output(LED1, GPIO.HIGH)
  GPIO.output(LED2, GPIO.HIGH)
  
  time.sleep(2)
  
  print('Light off')
  GPIO.output(LED1, GPIO.LOW)
  GPIO.output(LED2, GPIO.LOW)
  
print('Motion Sensor Alarm (CTRL+C to exit)')
time.sleep(.2)
print('Ready')


try:
  GPIO.add_event_detect(PIR_pin, GPIO.RISING, callback=LIGHTS)
  while 1:
    time.sleep(1)
except KeyboardInterrupt:
  print('Quit')
  GPIO.cleanup()

'''import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
PIR_pin = 17
LED_pin = 23
GPIO.setup(PIR_pin, GPIO.IN)
GPIO.setup(LED_pin, GPIO.OUT)
while True:
  i=GPIO.input(PIR_pin)
  if i==0:
    print 'No intruders', i
    GPIO.output(LED_pin, 0)
    time.sleep(0.1)
  elif i==1:
    print 'Intruder detected', i
    GPIO.output(LED_pin, 1)
    time.sleep(0.1)
'''


#print "Waiting for sensor to settle"
#time.sleep(2)
#print "Detecting motion"
#while True:
#  if GPIO.input(PIR_pin):
#    print "Motion Detected!"
#    time.sleep(2)
#  time.sleep(0.1)
