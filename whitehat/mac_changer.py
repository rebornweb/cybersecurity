#!/usr/bin/env python

import subprocess
import optparse

def capture_input():
    #If no options given use input
    interface = input(" interface > ") 
    new_mac = input(" New MAC address > ")
    return interface, new_mac

def get_args():
    
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()


def change_mac(interface, new_mac):
    print("[+] Changing Mac Address for: " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

(options,arguments) = get_args() 
(interface, new_mac) = capture_input()

change_mac(options.interface or interface, options.new_mac or new_mac)
