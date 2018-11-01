# Attini Environment

## Client to Raspberry Pi 3 (RPi3)

**Author:** Fernando de Assis Rodrigues 
**Contact:** fernando at rodrigues dot pro dot br
**Project from:** [dadosabertos.info](http://dadosabertos.info/projects/attini)

## Clean installation

### Requirements
+ Raspberry Pi 3 
+ Updated Raspbian distro with a seeting wi-fi and SSH access

### Clean installation Recipe

We suggest to use /opt/attini as default path installation.
This is the 101 recipe to a clean installation on RPi3/Raspbian:
`
sudo apt-get install git python3-pip -y
cd ~/
git clone https://github.com/rodriguesprobr/attini_client_rpi3.git
sudo mkdir -p /opt/attini
sudo chown pi:pi /opt/attini
mv attini_client_rpi3 /opt/attini/client
sudo -H pip3 install /opt/attini/client
`
Also, you may be able to schedule the client at the boot using cron capabilites, as mentioned above:
`
@reboot /usr/bin/python3 /opt/attini/client/attini.py start
`
