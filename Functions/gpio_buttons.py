#from https://github.com/MonomCZ/MeowPi-3
import RPi.GPIO as GPIO
import time

btn1 = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def button1():
    while True:
        if GPIO.input(btn1) == 1:
            return True
        else:
            return False