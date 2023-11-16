from scapy.all import *

sgw = conf.route.route("0.0.0.0")[2]
sgwm = getmacbyip(sgw)
print(sgw+"   "+sgwm)

def packet_list(packets):
    print("_"*100)
    print("")
    for x in range(len(packets)):
        print(x+1,": ",packets[x])
    print("")
    print("_"*100)
    print("")

def disp(packet):
    print("_"*100)
    print("(Ether) MAC: src: "+packet[Ether].src+" dst: "+packet[Ether].dst)
    if packet.haslayer(IP):
        print("(IPv4) IP: src: "+packet[IP].src+" dst: "+packet[IP].dst)
    if packet.haslayer(TCP):
        print("(TCP) Port: src: "+str(packet[TCP].sport)+" dst: "+str(packet[TCP].dport))        
    if packet.haslayer(Raw):
        print("(Raw) Load: "+str(packet[Raw].load)) 
    print("_"*100)

def mod_packets(packet, packets):
    disp(packet)
    l = "Ether "
    if packet.haslayer(IP):
#        src_ip = packet[IP].src
#        dst_ip = packet[IP].dst
        l = l+"IP "
    if packet.haslayer(TCP):
#        src_port = packet[TCP].sport
#        dst_port = packet[TCP].dport
        l = l+"TCP "
    if packet.haslayer(Raw):
        l = l+"RAW"
    l = l+": "
    t = input(l)
    while t != "":
        if t == "mac":
            packet[Ether].dst = input("mac: ")
        if t == "ip":
            packet[IP].dst = input("ip: ")
        if t == "raw":
            packet[Raw].load = input("raw: ")
        if t == "d":
            disp(packet)
        t = input(l)
    t = input("s/: ")
    if t == "s":
        sendp(packet, verbose=False)
    if t == "":
        exam(packets)


def exam(packets):
    packet_list(packets)
    x = None
    while x != -1 :
        x = input("explore packet: ")
        if x == "":
            hoofd()
        x = int(x)-1
        if x > -1:
            packet = packets[x]
            t = None
            while t != "":
                print("")
                print(packet.summary())
                t = input("s(show) / h(hexdump) /m(mod): ")
                print("")
                if t == "s":
                    packet.show()
                if t == "h":
                    hexdump(packet)
                if t =="m":
                    mod_packets(packet, packets)
            packet_list(packets)


def hoofd():
    f = input("filter: ")
    aantal = (input("count: "))
    if aantal == "":
        aantal = 0
    packets = sniff(count=int(aantal), filter=f, prn=lambda x: x.summary())
    exam(packets)

hoofd()

#TCP port 80