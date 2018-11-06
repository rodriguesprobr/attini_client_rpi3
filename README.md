# Attini Environment

[Server (Linux x64 - Python 3.5+ - MySQL/MariaDB)](https://github.com/rodriguesprobr/attini_server "Attini Server x64") | [Client RPi3 (Linux arm - Python 3.5+)](https://github.com/rodriguesprobr/attini_client_rpi3 "Attini Client - RPi 3")

## Client to Raspberry Pi 3 (RPi3)

**Author:** Fernando de Assis Rodrigues 
**Contact:** fernando at rodrigues dot pro dot br
**Project from:** [dadosabertos.info](http://dadosabertos.info/projects/attini)

## Clean installation

### Requirements
+ Raspberry Pi 3 
+ Updated Raspbian distro with a set-up wi-fi and SSH access

### Clean installation Recipe

We suggest to use /opt/attini as default path installation.
This is the 101 recipe to a clean installation on RPi3/Raspbian:
```
sudo apt-get install git python3-pip python3-dev libsdl1.2-dev libsdl-image1.2 -y
cd ~/
git clone https://github.com/rodriguesprobr/attini_client_rpi3.git
sudo mkdir -p /opt/attini
sudo chown pi:pi /opt/attini 
mv attini_client_rpi3 /opt/attini/client
sudo -H pip3 install /opt/attini/client

You can test some parts of attini system with the follwing scripts:
```
/usr/bin/python3 /opt/attini/client/test-lights.py
/usr/bin/python3 /opt/attini/client/test-sensors.py
/usr/bin/python3 /opt/attini/client/test-connection.py
```

Also, you may be able to schedule the client at the boot using cron capabilites, as mentioned above:
```
@reboot /usr/bin/python3 /opt/attini/client/attini.py start
```

## Troubleshootings

### Timelapse

- Be sure that image and video path are writable. You may also setting the paths to those dirs in config.json file.
