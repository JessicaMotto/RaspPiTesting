import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
PIR_pin = 11
LED_pin = 3
GPIO.setup(PIR_pin, GPIO.IN)
GPIO.setup(LED_pin, GPIO.OUT)
while True:
  i=GPIO.input(PIR_pin)
  if i==0
    print 'No intruders', i
    GPIO.output(LED_pin, 0)
    time.sleep(0.1)
  elif i==1
    print 'Intruder detected', i
    GPIO.output(LED_pin, 1)
    time.sleep(0.1)



#print "Waiting for sensor to settle"
#time.sleep(2)
#print "Detecting motion"
#while True:
#  if GPIO.input(PIR_pin):
#    print "Motion Detected!"
#    time.sleep(2)
#  time.sleep(0.1)
