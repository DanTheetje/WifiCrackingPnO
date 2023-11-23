import scapy.all as scapy


scapy_cap = scapy.rdpcap("WEPdummyPacket.pcap")
for packet in scapy_cap:
    print(packet[IPv6].src)

# Function to convert ASCII to hex
def ascii_to_hex(text):
    hex_result = ''.join(hex(ord(char))[2:] for char in text)
    return hex_result


key = ascii_to_hex(input("wat is de key?")) # dit is ascii
print(key)

hex_string = input("Wat is de hex data van de package?")

# stap 1: IV strippen

def get_IV_from_Data():
    pass


IV = get_IV_from_Data()


S = range(256)
j = 0
out = []
"""
#KSA Phase
for i in range(256):
    j = (j + S[i] + ord( key[i % len(key)] )) % 256
    S[i] , S[j] = S[j] , S[i]

#PRGA Phase
i = j = 0
for char in data:
    i = ( i + 1 ) % 256
    j = ( j + S[i] ) % 256
    S[i] , S[j] = S[j] , S[i]
    out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

print("".join(out))
"""