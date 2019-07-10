#!/usr/bin/env python

import subprocess

interface = input("Interface: ")
new_mac = input("new MAC: ")

print(" [+] Changing MAC Address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
#subprocess.call("ifconfig " + interface + " hw ether 08:00:27:89:03:db", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac , shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)


