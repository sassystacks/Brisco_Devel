import serial

ser = serial.Serial('ACM0',9600)

while(1)
    ser.printline()
