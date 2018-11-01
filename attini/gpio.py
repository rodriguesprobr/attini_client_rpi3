#!/usr/bin/python
# -*- coding: utf8 -*-
# Dúvidas sobre o funcionamento das Portas da GPIO: http://raspi.tv/2013/rpi-gpio-basics-4-setting-up-rpi-gpio-numbering-systems-and-inputs
# Dúvidas sobre os nomes de cada porta: https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/
# Atenção: O padrão adtoado é o nome da GPIO.
from attini import util

import Adafruit_DHT
import base64
import pygame
import pygame.camera
import RPi.GPIO as GPIO

def blink(port, qty, speed):
    if qty > 0:
        light(port, 1)
        util.sleep(speed, speed)
        light(port, 0)
        util.sleep(speed, speed)
        blink(port, (qty - 1), speed)
        
def light(port, status):
    if status == 1:
        GPIO.output(port, 3)
    else:
        GPIO.output(port, 0)
        
def get_rpiid():
    rpiid = "0000000000000000"
    try:
        f = open('/proc/cpuinfo','r')
        for l in f:
            if l[0:6]=='Serial':
                rpiid = l[10:26]
        f.close()
    except:
        rpiid = False
    return rpiid
    
def start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(util.get_config("red_led_port"), GPIO.OUT)
    GPIO.setup(util.get_config("green_led_port"), GPIO.OUT)
    GPIO.setup(util.get_config("blue_led_port"), GPIO.OUT)
    
def cleanup():
    GPIO.cleanup()
    
def read(sensor_type, port):
    if sensor_type == "DHT11":
        return Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, port)
    elif sensor_type == "FC28":
        GPIO.setup(port, GPIO.IN)
        return GPIO.input(port)
    elif sensor_type == "CameraUSB":
        try:
            pygame.camera.init()
            cam = pygame.camera.Camera("/dev/video0",(640,480))
            cam.start()
            photo_bin = cam.get_image()
            pygame.image.save(photo_bin,"temp.jpg")
            cam.stop()
            with open("temp.jpg", "rb") as photo_file:
                photo_bin_64 = base64.b64encode(photo_file.read())
            return photo_bin_64
        except:
            return False
    else:
        return False
