#!/usr/bin/env python

import subprocess
import re
import argparse

def get_argy():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_argument("-m","--mac", dest="new_mac", help="New MAC address")
    args = parser.parse_args()
    if not args.interface and not args.new_mac:
        args.interface = input(" interface > ") 
        args.new_mac = input(" New MAC address > ")   
    elif not args.interface:
        parser.error("[-] No interface entered")
    elif not args.new_mac:
        parser.error("[-] No MAC entered")
    return args

def change_mac(interface, new_mac):
    print("[+] Changing Mac Address for: " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_regex = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode('utf-8'))

    if mac_address_regex:
        return mac_address_regex.group(0)
    else:
        print("[-] Could not read MAC address")
   
(args) = get_argy()
currentmac = get_current_mac(args.interface)

print("Current MAC address: " + str(currentmac))

change_mac(args.interface, args.new_mac)
checkmac = get_current_mac(args.interface)

#Validation
if checkmac == args.new_mac:
    print("[+] MAC address was successfully changed to " + checkmac)
elif checkmac != args.new_mac:
    print("[-] MAC address change was unsuccessful")
