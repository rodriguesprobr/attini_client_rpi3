from attini import gpio
from attini import util

import requests

def send(air_humidity, air_temperature, soil_moisture, photo_bin):
    util.log("Sent package over HTTP to {0}:{1}".format(\
        util.get_config('server_ip'),\
        str(util.get_config('server_port'))\
    ), "attini/transmission.py")
    result = 0
    try:
        data = {
            "rpiid" : gpio.get_rpiid(),
            "air_humidity" : air_humidity,
            "air_temperature" : air_temperature,
            "soil_moisture" : soil_moisture
        }
        files = {
            "photo_bin" : ("0" if photo_bin == False else photo_bin)
        }
        response = requests.post(\
            "http://" + util.get_config('server_ip') + ":" + str(util.get_config('server_port')),\
            data = data,\
            files = files,\
            timeout = 10\
        )
        util.log("HTTP response status code {0}".format(str(response.status_code)), "attini/transmission.py")
        if response.status_code == requests.codes.ok:
            util.log("Data sent.")
            try:
                result = int(response.text)
            except:
                result = -1
        else:
            util.log("Error sending data to server.", "attini/transmission.py")
        return result
    except requests.exceptions.ReadTimeout:
        util.log("Error sending data to server. Connection timeout.", "attini/transmission.py")
        return result
    except (requests.exceptions.ConnectionError):
        util.log("Error sending data to server. Connection error.", "attini/transmission.py")
        return result