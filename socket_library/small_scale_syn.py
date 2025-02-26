from scapy.all import IP, TCP, send
import time

# Target details
target_ip = "172.16.98.225"
target_port = 80

# Craft a TCP SYN packet
syn_packet = IP(dst=target_ip) / TCP(dport=target_port, flags="S")

# Send the SYN packet
for i in range (0,50):
    send(syn_packet, verbose=True)
    time.sleep(0.3)