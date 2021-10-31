#!/usr/bin/python37all


import PCF8591 as ADC
from stepper import *
import time
import RPi.GPIO as GPIO

# access address for photoresistor
ADC.setup(0x48)

GPIO.setmode(GPIO.BCM)
pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
for pin in pins:
 GPIO.setup(pin, GPIO.OUT, initial=0)

# set LED pin to output
GPIO.setup(26, GPIO.OUT)

# halfstep cycle for ccw rotation
ccw = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]

# improve time resolution by using microseconds
def delay_us(tus): 
 endTime = time.time() + float(tus)/ float(1E6)
 while time.time() < endTime:
  pass

# create a list for html values to go into
data = {}

while True:
 with open('stepper_control.txt', 'r') as f:
   a = f.readline()
   b = f.readline()

 a = a.rstrip('\n')

 data[0] = int(a)
 data[1] = int(b)

 print(data)


 if (data[1]==1):
   stepper_motor.zero()
   current_degree = 0

 else:
   new_degrees = data[0] - current_degree
   stepper_motor.angle(new_degrees)
   current_degree = data[0]

  


  