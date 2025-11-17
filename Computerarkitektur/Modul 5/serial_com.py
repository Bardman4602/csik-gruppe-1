import serial

ser=serial.Serial('COM8',9600,timeout=1)

ser.write("tekst".encode("utf-8"))
ser.write(bytes([0x00,0xFF]))
ser.write(bytes([0,255]))
          
recieve = ser.readline()