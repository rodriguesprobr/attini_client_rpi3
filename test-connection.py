#!/usr/bin/python
# -*- coding: utf8 -*-
from attini import gpio
from attini import transmission
from attini import util
import subprocess
import sys
if __name__ == '__main__':
    try:
        util.log("Trying to reach Google DNS at the address 8.8.8.8.", "test-connection.py", "debug")
        ping_response = subprocess.Popen(["/bin/ping", "-c1", "-w100", "8.8.8.8"], stdout=subprocess.PIPE).stdout.read()
        if ping_response == 0:
            util.log("Fatal Error: Attini client is offline.", "test-connection.py", "debug")
        else:
            util.log("OK", "test-connection.py", "debug")
            util.log("Trying to reach Attini Server at the address {0}.".format(util.get_config("server_ip")), "test-connection.py", "debug")
            ping_response = subprocess.Popen(["/bin/ping", "-c1", "-w100", util.get_config("server_ip")], stdout=subprocess.PIPE).stdout.read()
            if ping_response == 0:
                util.log("Fatal Error: Attini server is offline.", "test-connection.py", "debug")
            else:
                util.log("OK", "test-connection.py", "debug")
                air_humidity = 30.5
                air_temperature = 30.5
                soil_moisture = True
                photo_bin = False
                
                util.log("Capturing photo from the USB Webcam.", "test-connection.py", "debug")
                photo_bin = gpio.read("CameraUSB", "")

                util.log("Transmitting data...", "test-connection.py", "debug")
                send_status = transmission.send(
                    air_humidity,
                    air_temperature,
                    soil_moisture,
                    photo_bin
                )
                if send_status == 0:
                    util.log("send_status == 0 -> Everything works fine.", "test-connection.py", "debug")
                elif send_status == -2:
                    util.log("send_status == -2 -> Everything works fine, but the photo was not transmitted . Error: {0}".format(str(send_status)), "test-connection.py", "debug")
                elif send_status == -30:
                    util.log("send_status == {0} -> Connection Error (Client is offline or Server is down). Error: {0}".format(str(send_status)), "test-connection.py", "debug")
                else:
                    util.log("send_status == {0} -> Error: {0}".format(str(send_status)), "test-connection.py", "debug")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        util.log("Exception: {0}".format(str(e)), "test-connection.py", "debug")
        pass
    finally:
        util.log("Finally", "test-connection.py", "debug")
