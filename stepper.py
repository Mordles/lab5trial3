#!/usr/bin/python37all

import RPi.GPIO as GPIO
import PCF8591 as ADC
import time

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




# create stepper class
class Stepper:
 """
 def __init__(self, pin1, pin2, pin3, pin4):
    self.phase1 = pin1
    self.phase2 = pin2
    self.phase3 = pin3
    self.phase4 = pin4
    """


 def zero(self):
   GPIO.output(26, 1)

   time.sleep(0.1)
   while (ADC.read(0) < 200):
     # move motor to zero
     for i in range(512): # full revolution (8     cycles/rotation * 64 gear ratio)
      for halfstep in range(8): # 8 half-steps per cycle
       for pin in range(4):    # 4 pins that need to be energized
         GPIO.output(pins[pin], ccw[halfstep][pin])
       delay_us(1000)
  
     print(ADC.read(0))
     ADC.write(ADC.read(0))
   GPIO.output(26, 0)
   print("Zero Found")
   
   s1 = '0'
   button = '0'

   with open('stepper_control.txt', 'w') as f:
     f.write(s1)
     f.write('\n')
     f.write(button)
     
   



 def angle(self,degrees):
   
   steps = int((degrees*512)/360)
   for i in range(steps):
     for halfstep in range(8):
      for pin in range(4):
       GPIO.output(pins[pin], ccw[halfstep][pin])
      delay_us(1000)
    

stepper_motor = Stepper()


   