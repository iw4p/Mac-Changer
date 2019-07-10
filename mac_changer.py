#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig", shell=True)

subprocess.call("ifconfig eth0 down", shell=True)

#subprocess.call("ifconfig eth0 hw ether 08:00:27:89:03:db", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:55", shell=True)

subprocess.call("ifconfig eth0 up", shell=True)

subprocess.call("ifconfig", shell=True)

