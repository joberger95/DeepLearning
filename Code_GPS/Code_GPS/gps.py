# gps frame used for test : $GPGGA,064036.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E
# from Wikipedia

import initSerial
from serial import SerialException


class Gps:
    def __init__(self):
        while initSerial.ser.isOpen():
            gps_frame = str(initSerial.ser.readlines(1))
            # print(gps_frame)
            self.frame_treatment(gps_frame)

    def frame_treatment(self, gps_frame):
        gps_frame = gps_frame.replace(",", "\x7F")
        time = gps_frame[9:20]
        hours = time[:3]
        minutes = time[3:5]
        seconds = time[5:7]
        print(f"{hours}h {minutes}m {seconds}s")
        latitude = gps_frame[20:32]
        longitude = gps_frame[32:45]
        print(f"\nLatitude {latitude}  \nLongitude {longitude}")


if __name__ == "__main__":
    Gps()
