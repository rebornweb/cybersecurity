#!/usr/bin/env python

import scapy.all as scapy
import argparse

def get_argy():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip","--address", dest="ip", help="IP address to scan ex. 192.168.0.1/24")
    args = parser.parse_args()
    if not args.ip:
        args.ip = input(" IP address > ") 
    return args


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list
        

def print_result(results_list):
    print("IP\t\t\tMAC address\n####################")  
    
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])
    print('####################')

(args) = get_argy()

result = scan(args.ip)
print_result(result)