from attini import gpio
from attini import util

import json
import requests

def send(air_humidity, air_temperature, soil_moisture, photo_bin):
    util.log("Sent package over HTTP to {0}:{1}".format(\
        util.get_config('server_ip'),\
        str(util.get_config('server_port'))\
    ), "attini/transmission.py")
    result = 0
    try:
        response = requests.post(\
            "http://" + util.get_config('server_ip') + ":" + str(util.get_config('server_port')),\
            data = json.dumps({
                "id" : gpio.get_id(),\
                "air_humidity" : air_humidity,\
                "air_temperature" : air_temperature,\
                "soil_moisture" : soil_moisture,\
                "photo_bin" : "0" if photo_bin == 0 else photo_bin.decode('utf-8')\
            }),\
            headers = {\
                "content-type" : "application/json"\
            },\
            timeout = 10\
        )
        util.log("HTTP response status code {0}".format(str(response.status_code)), "attini/transmission.py")
        if response.status_code == requests.codes.ok:
            util.log("Data sent.")
            try:
                result = '{' + response.text.split('{', 1)[1]
                util.log("Received data: {0}".format(str(result)), "attini/transmission.py")
            except:
                result = "{\"code\":\"-12\", \"message\":\"Error parsing the data received from attini server. Data: {0}\"}".format(str(response.text))
        else:
            util.log("Error sending data to server.", "attini/transmission.py")
        return json.loads(result)
    except requests.exceptions.ReadTimeout:
        util.log("Error sending data to server. Connection timeout.", "attini/transmission.py")
        return json.loads("{\"code\":\"-11\", \"message\":\"Error sending data to server. Connection timeout.\"}")
    except (requests.exceptions.ConnectionError):
        util.log("Error sending data to server. Connection error.", "attini/transmission.py")
        return json.loads("{\"code\":\"-10\", \"message\":\"Error sending data to server. Connection error.\"}")
