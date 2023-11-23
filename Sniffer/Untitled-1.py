from scapy.all import *
from cryptography.fernet import Fernet
sgw = conf.route.route("0.0.0.0")[2]
target_ip = sgw + "/24"
arp = ARP(pdst=target_ip)
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
result = srp(ether/arp, timeout=3, verbose=0)[0]
clients = []
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

for client in clients:
    if client['ip'] == sgw:
        print(client['ip']+ " "*8+client['mac']+" *")
    else:
        print(client['ip']+ " "*8+client['mac'])


#m = getmacbyip(ip)
#print(ip, m)
IFACES.show()
iface = IFACES.dev_from_index(input("index: "))

# Define the encryption key
key = b'your_secret_key_here'

def packet_handler(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"IP Packet: Source IP={src_ip}, Destination IP={dst_ip}")

    if packet.haslayer(TCP):
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        print(f"TCP Packet: Source Port={src_port}, Destination Port={dst_port}")

        if packet.haslayer(Raw):
            raw_data = packet[Raw].load
            try:
                decrypted_data = Fernet(key).decrypt(raw_data).decode("utf-8")
                print(f"Decrypted Data: {decrypted_data}")
            except Exception as e:
                print(f"Decryption error: {e}")

    if packet.haslayer(UDP):
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport
        print(f"UDP Packet: Source Port={src_port}, Destination Port={dst_port}")
    
    print("-" * 50)

sniff(iface=iface, prn=packet_handler, filter="tcp or udp")