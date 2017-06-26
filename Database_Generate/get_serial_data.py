import serial

ser = serial.Serial('/dev/ttyUSB0',9600)

while(1)
    a = ser.printline()
    b = a.split()[0]
    print(b)
    print(type(b))
