# Echo server program
import SocketServer
import RPi.GPIO as GPIO
import time

HOST = '192.169.0.2'                 # Symbolic name meaning all available interfaces
PORT =  50008             # Arbitrary non-privileged port

ac = 5
tamp = 6
bat= 21
in1 = 13
in2 = 19
in3 = 26

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(ac, GPIO.OUT)
    GPIO.setup(tamp, GPIO.OUT)
    GPIO.setup(bat, GPIO.OUT)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    
except:
    print("Unexpected error GPIO.setup:")
    
    

fAc= "AcFiluer"
fTamp= "Tamper"
fBat= "BatteryFailuer"
fInput= "Input"
            

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

print('Connected by', addr)
while True:
    data = conn.recv(1024)
    
    print (data)
    if data == fAc:
        GPIO.output(tamp, 1)
        conn.sendall(data + "-done")
        print ('tamper is on')
    if data == fTamp:
        GPIO.output(tamp, 1)
        conn.sendall(data + "-done")
        print ('tamper is on')
        

conn.close()
GPIO.output(tamp, 0)
GPIO.output(ac, 0)
GPIO.output(bat, 0)
