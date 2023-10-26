import serial
import datetime

#Change UART port number
ser = serial.Serial("/dev/cu.usbserial-0001", baudrate=115200, timeout=0.001)
ser.flushInput()
ser.flushOutput()
idx = 0

nmea_data = b""

# skip first line, since it could be incomplete
ser.readline()

while True:
    while ser.inWaiting():
        idx += 1
        nmea_sentence = ser.readline()
        # nmea_data += nmea_sentence

        print(f"{idx}: \n {nmea_sentence}")

        # if idx % 100 == 0:
        #     print(f"idx: {idx}")
            
        # if idx % 2000 == 0:

        #     # save to file after 2000 sentences added
        #     filename = datetime.datetime.utcnow().strftime("data/gps_data_%Y%m%d-%H%M%S.nmea")
        #     f = open(filename, "ab")
        #     f.write(nmea_data)
        #     f.close()
            
        #     nmea_data = b""