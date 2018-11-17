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
                air_humidity = -99.9
                air_temperature = -99.9
                soil_moisture = -99.9
                photo_bin = 0
                
                #util.log("Capturing photo from the USB Webcam.", "test-connection.py", "debug")
                #photo_bin = gpio.read("CameraUSB", "")
                img_path = "{0}/temp.jpg".format(util.get_config("photo_temp_path"))
                with open(img_path, "rb") as photo_file:
                    photo_bin = base64.b64encode(photo_file.read())

                util.log("Transmitting data...", "test-connection.py", "debug")
                result = transmission.send(
                    air_humidity,
                    air_temperature,
                    soil_moisture,
                    photo_bin
                )
                if int(result["code"]) == 0:
                    util.log("Everything works fine. Server response: {0} - {1}".format(result["code"], result["message"]), "test-connection.py", "debug")
                else:
                    util.log("Error. Server response: {0} - {1}".format(result["code"], result["message"]), "test-connection.py", "debug")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        util.log("Exception: {0}".format(str(e)), "test-connection.py", "debug")
        pass
    finally:
        util.log("Finally", "test-connection.py", "debug")
