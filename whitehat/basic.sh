#!/bin/bash
#traceroute google.com
#dig -t SOA w3schools.com

#Change mac
ifconfig eth0 down
ifconfig eth0 hw ether 00:11:22:33:44:55
ifconfig eth0 up
