#!/usr/bin/env python

import subprocess
import optparse
import re

def get_args():
    
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    
    if not options.interface and not options.new_mac:
        options.interface = input(" interface > ") 
        options.new_mac = input(" New MAC address > ")   
    elif not options.interface:
        parser.error("[-] No interface entered")
    elif not options.new_mac:
        parser.error("[-] No MAC entered")
    return options
     
def change_mac(interface, new_mac):
    print("[+] Changing Mac Address for: " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_regex = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode('utf-8'))

    if mac_address_regex:
        print('Mac address changed to: ' + mac_address_regex.group(0))
    else:
        print("[-] Could not read MAC address")
    return mac_address_regex.group(0)

(options) = get_args() 
currentmac = get_current_mac(options.interface)
print("Current MAC address: " + str(currentmac))
# change_mac(options.interface, options.new_mac)
