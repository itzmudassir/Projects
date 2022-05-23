#Traffic Lights System
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
r1 = 2  #Right Side red light
y1 = 3  #Right Side yellow light
g1 = 4  #Right Side green light
r2 = 5  #Left Side red light
y2 = 6  #Left Side yellow light
g2 = 7  #Left Side green light
yellow_delay = 2  #Delay for yellow light
delay = 5 #Delay for red & green light

#Set GPIO pins as output
GPIO.setup(r1, GPIO.OUT) #Set red light as output
GPIO.setup(y1, GPIO.OUT) #Set yellow light as output
GPIO.setup(g1, GPIO.OUT) #Set green light as output
GPIO.setup(r2, GPIO.OUT) #Set red light as output
GPIO.setup(y2, GPIO.OUT) #Set yellow light as output
GPIO.setup(g2, GPIO.OUT) #Set green light as output

#Traffic light system in a loop
while(True):
    print("Right Lane")    #Prints the right lane
    GPIO.output(r1, GPIO.HIGH) #Turn on red light
    GPIO.output(g2, GPIO.HIGH) #Turn on green light
    time.sleep(delay)  #Delay for red & green light
    GPIO.output(r1, GPIO.LOW) #Turn off red light
    GPIO.output(g2, GPIO.LOW) #Turn off green light
    print("Waiting for traffic light to change")  #Prints the waiting for traffic light to change
    GPIO.output(y1, GPIO.HIGH)  #Turn on yellow light
    GPIO.output(y2, GPIO.HIGH)  #Turn on yellow light
    time.sleep(yellow_delay)    #Delay for yellow light
    GPIO.output(y1, GPIO.LOW)   #Turn off yellow light
    GPIO.output(y2, GPIO.LOW)   #Turn off yellow light
    print("Left Lane")   #Prints the left lane
    GPIO.output(g1, GPIO.HIGH)   #Turn on green light
    GPIO.output(r2, GPIO.HIGH)   #Turn on red light
    time.sleep(delay)   #Delay for red & green light
    GPIO.output(g1, GPIO.LOW)   #Turn off green light
    GPIO.output(r2, GPIO.LOW)   #Turn off red light
    print("Waiting for traffic light to change")  #Prints the waiting for traffic light to change
    GPIO.output(y1, GPIO.HIGH) #Turn on yellow light
    GPIO.output(y2, GPIO.HIGH) #Turn on yellow light
    time.sleep(yellow_delay)  #Delay for yellow light
    GPIO.output(y1, GPIO.LOW) #Turn off yellow light
    GPIO.output(y2, GPIO.LOW) #Turn off yellow light
