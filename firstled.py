import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led = [5, 13 , 19 , 26]
while True:
	for i in led:
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i,1)
		print i
		time.sleep(3)
		GPIO.output(i, 0)
		time.sleep(1)
	time.sleep(60)


