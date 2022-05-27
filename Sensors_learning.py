#Sensors Learning
import RPi.GPIO as GPIO   #Import GPIO library
import time      #Import time module
GPIO.setmode(GPIO.BCM)   #Set GPIO pin numbering mode to BCM
GPIO.setwarnings(False)  #Disable warnings

#Variables for the GPIO pins
ir_sensor = 2  #IR sensor pin  
buzzer = 3    #Buzzer pin
redled = 17   #Red LED pin
greenled = 21  #Green LED pin
p_button = 27  #Push button pin
hall_effect = 10  #Hall effect sensor pin

#Set GPIO pins as input or output
GPIO.setup(ir_sensor, GPIO.IN)  #Set IR sensor as input
GPIO.setup(buzzer, GPIO.OUT)    #Set buzzer as output
GPIO.setup(redled, GPIO.OUT)    #Set red LED as output
GPIO.setup(greenled, GPIO.OUT)  #Set green LED as output
GPIO.setup(p_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #Set push button as input with pull up resistor
GPIO.setup(hall_effect, GPIO.IN)   #Set hall effect sensor as input

#loop to check the status of the GPIO pins
while True:    #Loop forever

    #Check if the push button is pressed
    if (GPIO.input(p_button) == 0):
        GPIO.output(buzzer, GPIO.HIGH)  #Turn on buzzer
        time.sleep(0.5)
        GPIO.output(buzzer, GPIO.LOW)   #Turn off buzzer
        time.sleep(0.5)

    #Check if the hall IR sensor is triggered
    elif (GPIO.input(ir_sensor) == False):
        GPIO.output(redled, GPIO.HIGH)  #Turn on red LED
        GPIO.output(greenled, GPIO.LOW) #Turn off green LED
        time.sleep(0.5)
        GPIO.output(redled, GPIO.LOW)   #Turn off red LED
        time.sleep(0.5)

    #Check if the hall effect sensor is triggered
    elif (GPIO.input(hall_effect) == False):
        GPIO.output(greenled, GPIO.HIGH)  #Turn on green LED
        GPIO.output(redled, GPIO.LOW)     #Turn off red LED
        time.sleep(0.5)
        GPIO.output(greenled, GPIO.LOW)   #Turn off green LED
        time.sleep(0.5)