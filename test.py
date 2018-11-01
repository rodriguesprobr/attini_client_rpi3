#!/usr/bin/python
# -*- coding: utf8 -*-
from attini import gpio
from attini import transmission
from attini import util
import sys
if __name__ == '__main__':
    try:

        air_humidity = 30.5
        air_temperature = 30.5
        soil_moisture = True
        photo_bin = False
        
        util.log("Capturing photo from the USB Webcam.", "test.py", "debug")
        photo_bin = gpio.read("CameraUSB", "")

        util.log("Transmitting data...", "test.py", "debug")
        send_status = transmission.send(
            air_humidity,
            air_temperature,
            soil_moisture,
            photo_bin
        )
        if send_status == 0:
            util.log("send_status == 0 -> Everything works fine.", "test.py", "debug")
        elif send_status == -2:
            util.log("send_status == 1 -> Everything works fine, but the photo was not transmitted . Error: ".format(str(send_status)), "test.py", "debug")
        else:
            util.log("send_status == 2 -> Error: ".format(str(send_status)), "test.py", "debug")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        util.log("Exception: {0}".format(str(e)), "test.py", "debug")
        pass
    finally:
        util.log("Finally", "test.py", "debug")
