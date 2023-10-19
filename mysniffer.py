from scapy.all import *

def packet_list(packets):
    print("____________________________________________________________________")
    print("")
    for x in range(len(packets)):
        print(x+1,": ",packets[x])
    print("")
    print("____________________________________________________________________")
    print("")

def exam(packets):
    packet_list(packets)
    x = None
    while x != -1 :
        x = input("explore packet: ")
        if x != "":
            x = int(x)-1
        if x == "":
            hoofd()
        if x > -1:
            packet = packets[x]
            t = None
            while t != "":
                print("")
                print(packet.summary())
                t = input("s(show) / hd(hexdump) / hr(hexraw): ")
                print("")
                if t == "s":
                    packet.show()
                if t == "hd":
                    hexdump(packet)
                if t == "hr":
                    hexraw(packet)
            packet_list(packets)

def hoofd():
    f = input("filter: ")
    aantal = (input("count: "))
    if aantal == "":
        aantal = 0
    packets = sniff(count=int(aantal), filter=f, prn=lambda x: x.summary())
    exam(packets)

hoofd()

#host 163.182.194.25
#tcp
#udp
#port 25 or port 110

