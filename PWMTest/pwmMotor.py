import time
import os
import pigpio
import RPi.GPIO as GPIO
import signal
from xbox360controller import Xbox360Controller

signalPin = 10
GPIO.setmode(GPIO.BOARD)
GPIO.setup(signalPin, GPIO.OUT)

freq = 350 # 350hz = 30%- - 50%~n - 70%+

dc_min = 30
dc_max = 70
dc_n = 50
dc = 0

p = GPIO.PWM(signalPin, freq)
p.start(dc)

# def speed2dc():
# 	dc = dc_n + (speed*20)
# 	if dc > dc_n-1 and dc < dc_n+1:
# 		dc = 0
# 	elif dc < dc_min:
# 		dc = dc_min
# 	elif dc > dc_max:
# 		dc = dc_max
# 	p.ChangeDutyCycle(dc)
# 	print("Freqency: ", freq, "Duty Cycle: ", dc)

controller = Xbox360Controller(0, axis_threshold=0.2)
while(1):
	# randomVal = controller.axis_l._value_y
	# speed = float(input("Enter Speed [-1,1]: "))
	speed = controller.axis_l._value_y
	
	dc = dc_n + (speed*20)
	if dc > dc_n-1 and dc < dc_n+1:
		dc = 0
	elif dc < dc_min:
		dc = dc_min
	elif dc > dc_max:
		dc = dc_max
	p.ChangeDutyCycle(dc)
	print("L Axis: ",controller.axis_l._value_y,  "Freqency: ", freq, "Duty Cycle: ", dc)
	

#while (1):
#		j = 0
#		freq = 1
#		while(1):
#			# speed=float(input("How fast? dc: "))
#			# if (speed == -1):
#			# 	break
#			# p.ChangeDutyCycle(speed)
#			freq += 1
#			if freq > 2000:
#				break
#			p.ChangeFrequency(freq)
#			print("Duty Cycle: ", dc, "Frequency: ", freq)
#			time.sleep(0.01)
#
#		dc += 1
#		if dc > 100:
#			break
#		p.ChangeDutyCycle(dc)
#
#
#j = 0
#freq = 1
#dc = 70
#p.ChangeDutyCycle(dc)
#while(1):
#                freq += 1
#                if freq > 2000:
#                    break
#                p.ChangeFrequency(freq)
#                print("Duty Cycle: ", dc, "Frequency: ", freq)
#                time.sleep(0.1)

p.stop()
GPIO.cleanup()

