#Traffic Lights System
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
r1 = 2
y1 = 3
g1 = 4
r2 = 5
y2 = 6
g2 = 7
yellow_delay = 2  #Delay for yellow light
delay = 5 #Delay for red & green light
GPIO.setup(r1, GPIO.OUT)
GPIO.setup(y1, GPIO.OUT)
GPIO.setup(g1, GPIO.OUT)
GPIO.setup(r2, GPIO.OUT)
GPIO.setup(y2, GPIO.OUT)
GPIO.setup(g2, GPIO.OUT)
GPIO.output(r1, GPIO.HIGH)
while(True):
    print("Right Lane")
    GPIO.output(r1, GPIO.HIGH)
    GPIO.output(g2, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(r1, GPIO.LOW)
    GPIO.output(g2, GPIO.LOW)
    print("Waiting for traffic light to change")
    GPIO.output(y1, GPIO.HIGH)
    GPIO.output(y2, GPIO.HIGH)
    time.sleep(yellow_delay)
    GPIO.output(y1, GPIO.LOW)
    GPIO.output(y2, GPIO.LOW)
    print("Left Lane")
    GPIO.output(g1, GPIO.HIGH)
    GPIO.output(r2, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(g1, GPIO.LOW)
    GPIO.output(r2, GPIO.LOW)
    print("Waiting for traffic light to change")
    GPIO.output(y1, GPIO.HIGH)
    GPIO.output(y2, GPIO.HIGH)
    time.sleep(yellow_delay)
    GPIO.output(y1, GPIO.LOW)
    GPIO.output(y2, GPIO.LOW)

