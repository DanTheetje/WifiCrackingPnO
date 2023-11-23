import scapy
import pip

print(pip.__version__)
print(scapy.__version__)

my_frame = scapy.Ether() / scapy.IP()
my_frame.show()
print(my_frame)
print("____________________________________________________________")

packets = scapy.sniff(count=50)
packets.summary()
print("___________________________________________________________")
for x in range(50):
    print(packets[x])
print("____________________________________________________________")

# my_packets library aanmaken
my_packets = {}
my_packets[scapy.IP] = scapy.IP()
my_packets[scapy.Ether] = scapy.Ether()

def print_source_ethernet(frame):
    print(frame[scapy.Ether].src)

scapy.sniff(count = 2, prn = print_source_ethernet)

def is_broadcast_frame(frame):
    print(frame[scapy.Ether].dst)
    if frame[scapy.Ether].dst == "ff:ff:ff:ff:ff:ff":
        print("True")
        return "True"
    else:
        print("False")
        return "False"
    return frame[scapy.Ether].dst == "ff:ff:ff:ff:ff:ff"

print("_______________________________________________________________________________")
frames = scapy.sniff(count = 2, lfilter = is_broadcast_frame)
print(frames)
print(frames[0][scapy.Ether].dst)

print("_______________________________________________________________________________")
scapy.sniff(count = 2, prn = print_source_ethernet, lfilter= is_broadcast_frame)

print("*******************************************************************************")

frame = scapy.Ether(dst = 'aa:aa:aa:aa:aa:aa') / scapy.Raw("Hello world")
frame[scapy.Ether].dst = 'bb:bb:bb:bb:bb:bb'
frame.show()
scapy.hexdump(frame)

