"""
Scans the network for devices by sending ARP requests to the specified IP or IP range.

Args:
    ip (str): The target IP address or IP range to scan (e.g., "192.168.1.1/24").
    
Returns:
    list: A list of dictionaries, where each dictionary contains the IP and MAC address
          of a detected device. Example:
            [
                {"ip": "192.168.1.1", "mac": "00:11:22:33:44:55"},
                {"ip": "192.168.1.2", "mac": "66:77:88:99:AA:BB"}
            ]
"""

#!/usr/bin/env python

import scapy.all as scapy
import argparse  # [+] Instead of using python 2.7 optparse library


def get_arguments():
    parser = argparse.ArgumentParser()  # Instead of using optparse.OptionParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP or Target subnet")  # Instead of .addoption
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify the target IP or subnet, use -h or --help for more info")
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n--------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
