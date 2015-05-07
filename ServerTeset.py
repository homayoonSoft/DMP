# Echo server program
import socket

HOST = '192.168.0.5'                 # Symbolic name meaning all available interfaces
PORT =  50008             # Arbitrary non-privileged port

ac = 5
tamp = 6
bat= 21
in1 = 13
in2 = 19
in3 = 26
fAc= "AcFailuer"
fTamp= "Tamper"
fBat= "BatteryFailuer"
fInput= "Input"
fdata= fTamp            

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    print('connction wait ....')
    s.listen(1)
    conn, addr = s.accept()

    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        print (data)
        if data == fAc:
            conn.sendall(data + "-done")
            print ('tamper is on' /n)

        elif date == ftamp + "off":
            conn.sendall(data + "-off")
            print ('tamper is off' /n)
      
        else:
           print ('nothing')

except:
    print("Unexpected error:")      
         
finally:
    conn.close()
