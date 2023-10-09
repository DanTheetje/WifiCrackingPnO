import scapy
import pip
print(pip.__version__)
print(scapy.__version__)
from scapy.all import *
my_frame = Ether() / IP()
my_frame.show()
print(my_frame)
print("____________________________________________________________")

packets = sniff(count=50)
packets.summary()
print("___________________________________________________________")
for x in range(50):
    print(packets[x])
print("____________________________________________________________")

# my_packets library aanmaken
my_packets = {}
my_packets[IP] = IP()
my_packets[Ether] = Ether()

def print_source_ethernet(frame):
    print(frame[Ether].src)
    pass

sniff(count = 2, prn = print_source_ethernet)

def is_broadcast_frame(frame):
    print(frame[Ether].dst)
    if frame[Ether].dst == "ff:ff:ff:ff:ff:ff":
        print("True")
        return "True"
    else:
        print("False")
        return "False"
    return frame[Ether].dst == "ff:ff:ff:ff:ff:ff"

print("_______________________________________________________________________________")
frames = sniff(count = 2, lfilter = is_broadcast_frame)
print(frames)
print(frames[0][Ether].dst)

print("_______________________________________________________________________________")
sniff(count = 2, prn = print_source_ethernet, lfilter= is_broadcast_frame)

print("*******************************************************************************")

frame = Ether(dst = 'aa:aa:aa:aa:aa:aa') / Raw("Hello world")
frame[Ether].dst = 'bb:bb:bb:bb:bb:bb'
frame.show()
hexdump(frame)

