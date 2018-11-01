       _   _   _       _        _ _            _   
  __ _| |_| |_(_)_ __ (_)   ___| (_) ___ _ __ | |_ 
 / _` | __| __| | '_ \| |  / __| | |/ _ \ '_ \| __|
| (_| | |_| |_| | | | | | | (__| | |  __/ | | | |_ 
 \__,_|\__|\__|_|_| |_|_|  \___|_|_|\___|_| |_|\__|
                                                   
by Fernando de Assis Rodrigues 
fernando at rodrigues dot pro dot br

http://dadosabertos.info/projects/attini

We suggest to use /opt/attini as default path installation.

This is the 101 recipe to a shortcut installation:
cd ~/
git clone XXXX
sudo mkdir -p /opt/attini
sudo chown pi:pi /opt/attini
mv client /opt/attini/
sudo -H pip3 install /opt/attini/client

Also, you may be able to schedule the client at the boot using cron capabilites, as mentioned above:

@reboot /usr/bin/python3 /opt/attini/client/attini.py start 
