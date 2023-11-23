import scapy.all as scapy


WEP_packets = scapy.rdpcap("Sniffer/WEPdummyPacket.pcap") # dit kan later problemen veroorzaken
for packet in WEP_packets:
    WEP_packet = packet

# stap 1: IV, data, key vinden
IV_binary = WEP_packet[scapy.Dot11WEP].iv

WEPdata_binary = bytearray(WEP_packet.wepdata)

#scapy.hexdump(WEP_packet)
print(WEP_packet.wepdata.hex())
print(str(WEP_packet[scapy.Dot11WEP].iv.hex()))
# Function to convert ASCII to hex
def ascii_to_hex(text):
    hex_result = ''.join(hex(ord(char))[2:] for char in text)
    return hex_result


def generate_key_stream(ppk, iv, wepdata):
    #PPK moet in bits staan
    S = range(256)
    j = 0
    out = bytearray()
    lengte_bits = len(ppk)*8
    # KSA Phase
    for i in range(256):
        j = (j + S[i] + ppk[i % len(ppk)]) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA Phase
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

    return out


def wep_decrypt(ppk, iv, ciphertext):
    key_stream = generate_key_stream(ppk, iv, ciphertext)
    plaintext = bytearray()

    for i in range(len(ciphertext)):
        plaintext.append(ciphertext[i] ^ key_stream[i])

    return bytes(plaintext)

WEPkey_binary = bytes.fromhex(ascii_to_hex(input("wat is de key?"))) # dit is ascii
print(WEPkey_binary.hex())

ppk = IV_binary+WEPkey_binary
print(ppk)
print(len(ppk))

print(bytearray(ppk))
print(wep_decrypt(ppk,IV_binary,WEPdata_binary))