import sys
from scapy.all import *
import time

def packet_list(packets, aantal):
    if aantal == 0:
        aantal = len(packets)
    print("____________________________________________________________________")
    print("")
    for x in range(0,aantal):
        print(x+1,": ",packets[x])
    print("")
    print("____________________________________________________________________")
    print("")

def exam(packets, aantal):
    packet_list(packets, aantal)
    x = None
    while x != -2 :
        x = int(input("explore packet: "))-1
        if x > -1:
            packet = packets[x]
            t = None
            while t != "0":
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
            packet_list(packets, aantal)
        if x == -1:
            hoofd()

def hoofd():
    f = input("filter: ")
    aantal = int(input("packets: "))
    packets = sniff(count=aantal, filter=f, prn=lambda x: x.summary())
    exam(packets, aantal)

hoofd()

#host 163.182.194.25
#tcp
#udp
#port 25 or port 110


