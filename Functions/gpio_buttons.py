#from https://github.com/MonomCZ/MeowPi-3
import RPi.GPIO as GPIO
import time

btn1 = 22
btn2 = 5
btn3 = 24
btn4 = 27
btn5 = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def button1():
    while True:
        if GPIO.input(btn1) == 1:
            return True
        else:
            return False

            GPIO.setmode(GPIO.BCM)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def button2():
    while True:
        if GPIO.input(btn2) == 1:
            return True
        else:
            return False

def button4():
    while True:
        if GPIO.input(btn4) == 1:
            return True
        else:
            return False
def button5():
    while True:
        if GPIO.input(btn5) == 1:
            return True
        else:
            return False

def button3():
    while True:
        if GPIO.input(btn3) == 1:
            return True
        else:
            return False

while True:
    if button1():
        print("Button 1 pressed")
        time.sleep(0.5)
    if button2():
        print("Button 2 pressed")
        time.sleep(0.5)
    if button3():
        print("Button 3 pressed")
        time.sleep(0.5) 
    if button4():
        print("Button 4 pressed")
        time.sleep(0.5)
    if button5():
        print("Button 5 pressed")
        time.sleep(0.5)
