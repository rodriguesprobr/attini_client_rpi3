#!/usr/bin/python
# -*- coding: utf8 -*-
from attini import gpio
from attini import transmission
from attini import util
import sys
if __name__ == '__main__':
    args = sys.argv
    action = args[1]
    if action == "start":
        try:
            gpio.start()
            gpio.light(util.get_config("red_led_port"), 0)
            gpio.light(util.get_config("green_led_port"), 0)
            gpio.light(util.get_config("blue_led_port"), 1)
            
            while True:
                gpio.light(util.get_config("green_led_port"), 1)
                gpio.light(util.get_config("blue_led_port"), 0)
                
                air_humidity = 0
                air_temperature = 0
                soil_moisture = False
                photo_bin = False

                air_humidity, air_temperature = gpio.read("DHT11", util.get_config("sensor_air_temp_humidity_port"))
                soil_moisture = gpio.read("FC28", util.get_config("sensor_soil_moisture_port"))
                
                gpio.light(util.get_config("red_led_port"), 1)
                gpio.light(util.get_config("blue_led_port"), 1)
                photo_bin = gpio.read("CameraUSB", "")
                gpio.light(util.get_config("red_led_port"), 0)
                gpio.light(util.get_config("blue_led_port"), 0)
                
                if air_temperature is None:
                    gpio.light(util.get_config("green_led_port"), 0)
                    gpio.blink(util.get_config("red_led_port"), 1, 0.125)
                    gpio.light(util.get_config("green_led_port"), 1)
                if air_humidity is None:
                    gpio.light(util.get_config("green_led_port"), 0)
                    gpio.blink(util.get_config("red_led_port"), 2, 0.125)
                    gpio.light(util.get_config("green_led_port"), 1)
                if soil_moisture is None:
                    gpio.light(util.get_config("green_led_port"), 0)
                    gpio.blink(util.get_config("red_led_port"), 3, 0.125)
                    gpio.light(util.get_config("green_led_port"), 1)
                
                send_status = transmission.send(
                    air_humidity,
                    air_temperature,
                    soil_moisture,
                    photo_bin
                )
                if send_status == 0:
                    gpio.blink(util.get_config("green_led_port"), 5, 0.125)
                elif send_status < 0:
                    gpio.light(util.get_config("green_led_port"), 0)
                    gpio.blink(util.get_config("red_led_port"), 4, 0.125)
                    gpio.light(util.get_config("green_led_port"), 1)
                elif send_status == 1:
                    gpio.light(util.get_config("green_led_port"), 0)
                    gpio.blink(util.get_config("red_led_port"), 5, 0.125)
                    gpio.light(util.get_config("green_led_port"), 1)
                elif send_status == 2:
                    gpio.light(util.get_config("green_led_port"), 0)
                    gpio.blink(util.get_config("red_led_port"), 6, 0.125)
                    gpio.light(util.get_config("green_led_port"), 1)
                
                gpio.light(util.get_config("green_led_port"), 0)
                gpio.light(util.get_config("blue_led_port"), 1)
                util.log("Waiting ~60 seconds to loop.", "attini.py")
                util.sleep(55,65)
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            gpio.light(util.get_config("green_led_port"), 0)
            gpio.light(util.get_config("blue_led_port"), 0)
            gpio.blink(util.get_config("red_led_port"), 7, 0.125)
            gpio.light(util.get_config("blue_led_port"), 1)
            pass
        finally:
            gpio.cleanup()
            gpio.light(util.get_config("red_led_port"), 0)
            gpio.light(util.get_config("green_led_port"), 0)
            gpio.light(util.get_config("blue_led_port"), 0)
            gpio.blink(util.get_config("blue_led_port"), 3, 0.125)
