# Echo server program
import socket
import RPi.GPIO as GPIO
import time
try:
	HOST = '10.2.5.9'                 # Symbolic name meaning all available interfaces
	PORT =  50008             # Arbitrary non-privileged port

	ac = 5
	tamp = 6
	bat= 21
	in1 = 13
	in2 = 19
	in3 = 26

	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(ac, GPIO.OUT)
	GPIO.setup(tamp, GPIO.OUT)
	GPIO.setup(bat, GPIO.OUT)
	GPIO.setup(in1, GPIO.OUT)
	GPIO.setup(in2, GPIO.OUT)
	GPIO.setup(in3, GPIO.OUT)
	fAc= "AcFailuer"
	fTamp= "Tamper"
	fBat= "BatteryFailuer"
	fInput= "Input"
        
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	
	while True:

		print('connction wait ....')
		s.listen(1)
		
		conn, addr = s.accept()
	
		print('Connected by', addr)
		while True:
			data = conn.recv(1024)
			if not data: break
			
			print ('data from SC is : ',data)
			if data == fTamp:
				GPIO.output(tamp, 1)
				conn.sendall(data + "-done")
				print ('tamper is on')
				
			if data == (fTamp + "-off"):
				GPIO.output(tamp, 0)
				conn.sendall(data + "-off")
				print ('tamper is off' )

			if data == fAc:
				GPIO.output(ac, 1)
				conn.sendall(data + "-done")
				print ('ac is off' )

			if data == fAc + "-off":
				GPIO.output(ac, 0)
				conn.sendall(data + "-off")
				print ('AC is on' )

			if data == fBat:
				GPIO.output(bat, 1)
				conn.sendall(data + "-done")
				print ('Battery is off' )

			if data == fBat + "-off":
				GPIO.output(bat, 0)
				conn.sendall(data + "-off")
				print ('Batterry is on' /n)

			if data == fInput:
				print ('start input1')
				GPIO.output(in1, 1)
				print ('in2')
				GPIO.output(in2, 1)
				print ('in3')
				GPIO.output(in3, 1)
				print('alarm')
				conn.sendall(data + "-done")
				print ('Inputs are in alarm')
				time.sleep(10)
				GPIO.output(in1, 0)
				GPIO.output(in2, 0)
				GPIO.output(in3, 0)
			
            
except:
	print("Unexpected error:")      
         
finally:
	conn.close()
	GPIO.output(tamp, 0)
	GPIO.output(ac, 0)
	GPIO.output(bat, 0)
