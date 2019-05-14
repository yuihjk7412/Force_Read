import serial
import time
import numpy as np
import threading
import binascii

if __name__ == '__main__':
    port_Num = input('PLEASE INPUT THE PORT NUMBER(/dev/ttyUSB*):')
    request_Command = bytes.fromhex('01 03 01 C2 00 08 E4 0C')
    with serial.Serial("/dev/ttyUSB%d" % int(port_Num), 9600, timeout=0.2) as ser:
        print("Serial Port OK!")
    ser.close()
    while 1:
        with serial.Serial("/dev/ttyUSB%d" % int(port_Num), 9600, timeout=0.2) as ser:
            ser.write(request_Command)
            buf = ser.read(21)

        print(int.from_bytes(buf[3:7], signed=True, byteorder='big'))

        time.sleep(0)