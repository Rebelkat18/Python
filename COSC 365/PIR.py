import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.IN)         #Read output from PIR motion sensor

while True:
    i=GPIO.input(23)
    if i==0:                 #When output from motion sensor is LOW
        print ("No")
        time.sleep(0.1)
    elif i==1:               #When output from motion sensor is HIGH
        print ("Yes")
        time.sleep(0.1)