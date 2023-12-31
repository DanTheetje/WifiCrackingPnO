import scapy.all as scapy
# Function to convert ASCII to hex
def ascii_to_hex(text):
    hex_result = ''.join(hex(ord(char))[2:] for char in text)
    return hex_result


def generate_key_stream(ppk, wepdata):

    S = [x for x in range(256)] #(0,1,2,3,..255)
    j = 0
    key_stream = bytearray()

    # KSA
    for i in range(256): #
        j = (j + S[i] + ppk[i % len(ppk)]) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA
    i = j = 0
    for i in range(len(wepdata)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        key_stream.append(S[(S[i] + S[j]) % 256]) 

    return key_stream


def rc4_decrypt(ppk, ciphertext):

    key_stream = generate_key_stream(ppk, ciphertext)
    plaintext = bytearray()

    for i in range(len(ciphertext)):

        plaintext.append(ciphertext[i] ^ key_stream[i])

    return bytes(plaintext)

def decryptWEPandPrint(WEP_packet,WEPkey_ascii=None):

    #DOT11WEP protocol moet aanwezig zijn
    # stap 1: IV, data, key vinden
    IV_binary = WEP_packet[scapy.Dot11WEP].iv

    WEPdata_binary = bytearray(WEP_packet.wepdata)


    print("Encrypted Data of packet : 0x"+WEP_packet.wepdata.hex())
    print("IV: 0x"+str(WEP_packet[scapy.Dot11WEP].iv.hex()))

    if WEPkey_ascii == None:
        WEPkey_binary = bytes.fromhex(ascii_to_hex(input("\nWhat is the WEP key?"))) # invoer is ascii
    else: WEPkey_binary= bytes.fromhex(ascii_to_hex(WEPkey_ascii))

    ppk = IV_binary+WEPkey_binary
    print("Per packet key: "+str(ppk))

    decrypted_package_data = rc4_decrypt(ppk, WEPdata_binary)
    print("\nDecrypted package: "+str(decrypted_package_data)) # \x in de output betekend dat volgende 2 char hexadecimaal zijn

    # om alle tekens te vertalen: Zie tabel https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
    print("\nTo translate escape sequences: https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals")

def decryptWEP(WEP_packet,WEPkey_ascii=None):

    #DOT11WEP protocol moet aanwezig zijn
    # stap 1: IV, data, key vinden
    IV_binary = WEP_packet[scapy.Dot11WEP].iv

    WEPdata_binary = bytearray(WEP_packet.wepdata)

    if WEPkey_ascii == None:
        WEPkey_binary = bytes.fromhex(ascii_to_hex(input("\nWhat is the WEP key?"))) # invoer is ascii
    else: WEPkey_binary= bytes.fromhex(ascii_to_hex(WEPkey_ascii))

    ppk = IV_binary+WEPkey_binary

    decrypted_package_data = rc4_decrypt(ppk, WEPdata_binary)
    return decrypted_package_data

if __name__ == "__main__":
    # packet selecteren
    WEP_packets = scapy.rdpcap("WEPdummyPacket.pcap") # dit kan later problemen veroorzaken
    for packet in WEP_packets:
        WEP_packet = packet
    print("WEP packet has been successfully read")

    decryptWEPandPrint(WEP_packet,"ESAT2")
    print(decryptWEP(WEP_packet,"ESAT2"))
