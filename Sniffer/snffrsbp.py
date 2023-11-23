from scapy.all import *

pkl = PcapWriter("/home/kali/Desktop/WEPpackettest.pcap", append = True, sync = True)

def fil(p):
    if p.haslayer(Dot11):
        if p.type == 0 and p.subtype == 8:
            p.summary()
            pkl.write(p)

sniff(iface="wlan1", filter="ether src 74:da:38:eb:6f:dc", prn=fil, store=0)

##################################################################################################

from scapy.all import *

pkl = PcapWriter("/home/kali/Desktop/WEPpackettest.pcap", append = True, sync = True)

def fil(p):
    if p.haslayer(Dot11WEP):
        p.summary()
        pkl.write(p)

sniff(iface="wlan1", filter="ether src 74:da:38:eb:6f:dc", prn=fil, store=0)