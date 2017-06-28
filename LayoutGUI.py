import serial

ser = serial.Serial('COM3')

while (1):
    a = ser.readline()
    print(a)
