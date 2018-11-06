#!/usr/bin/python
# -*- coding: utf8 -*-
from attini import gpio
from attini import util
import sys
if __name__ == '__main__':
    try:
        util.log("Testing sensors...", "test-sensors.py", "debug")
        util.log("Starting GPIO...", "test-sensors.py", "debug")
        gpio.start()
        util.log("Air Humidity & Air Temperature...", "test-sensors.py", "debug")
        air_humidity, air_temperature = gpio.read("DHT11", util.get_config("sensor_air_temp_humidity_port"))
        util.log("Values: {0} (AirHumidity) - {1} (Air Temperature)".format(str(air_humidity), str(air_temperature)), "test-sensors.py", "debug")
        util.log("Soil Moisture...", "test-sensors.py", "debug")
        soil_moisture = gpio.read("FC28", util.get_config("sensor_soil_moisture_port"))
        util.log("Value: {0}".format(str(soil_moisture)), "test-sensors.py", "debug")
        util.log("USB Webcam (photo)...", "test-sensors.py", "debug")
        photo_bin = gpio.read("CameraUSB", "")
        if photo_bin != False:
            util.log("USB Webcam (photo) detected.", "test-sensors.py", "debug")
        else:
            util.log("USB Webcam (photo) NOT detected.", "test-sensors.py", "debug")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        util.log("Exception: {0}".format(str(e)), "test-sensors.py", "debug")
        pass
    finally:
        util.log("Finally", "test-sensors.py", "debug")
        util.log("Cleaning up GPIO...", "test-sensors.py", "debug")
        gpio.cleanup()
