#!/usr/bin/python
# -*- coding: utf8 -*-
from attini import gpio
from attini import util
import sys
if __name__ == '__main__':
    try:
        util.log("Testing lights...", "test-lights.py", "debug")
        util.log("Starting GPIO...", "test-lights.py", "debug")
        gpio.start()
        util.log("Blink", "test-lights.py", "debug")
        util.log("Red", "test-lights.py", "debug")
        gpio.blink(util.get_config("red_led_port"), 10, 0.125)
        util.log("Green", "test-lights.py", "debug")
        gpio.blink(util.get_config("green_led_port"), 10, 0.125)
        util.log("Blue", "test-lights.py", "debug")
        gpio.blink(util.get_config("blue_led_port"), 10, 0.125)
        util.log("On/Off", "test-lights.py", "debug")
        for i in range(1,5):
            util.log("Red", "test-lights.py", "debug")
            gpio.light(util.get_config("red_led_port"), 1)
            util.sleep(1, 1)
            gpio.light(util.get_config("red_led_port"), 0)
            util.log("Green", "test-lights.py", "debug")
            gpio.light(util.get_config("green_led_port"), 1)
            util.sleep(1, 1)
            gpio.light(util.get_config("green_led_port"), 0)
            util.log("Blue", "test-lights.py", "debug")
            gpio.light(util.get_config("blue_led_port"), 1)
            util.sleep(1, 1)
            gpio.light(util.get_config("blue_led_port"), 0)
            util.log("White", "test-lights.py", "debug")
            gpio.light(util.get_config("red_led_port"), 1)
            gpio.light(util.get_config("green_led_port"), 1)
            gpio.light(util.get_config("blue_led_port"), 1)
            util.sleep(1, 1)
            gpio.light(util.get_config("red_led_port"), 0)
            gpio.light(util.get_config("green_led_port"), 0)
            gpio.light(util.get_config("blue_led_port"), 0)
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        util.log("Exception: {0}".format(str(e)), "test-lights.py", "debug")
        pass
    finally:
        util.log("Finally", "test-lights.py", "debug")
        util.log("Cleaning up GPIO...", "test-lights.py", "debug")
        gpio.cleanup()
