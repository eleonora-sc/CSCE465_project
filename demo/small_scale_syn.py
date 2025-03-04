from scapy.all import IP, TCP, send
import time

# Target details
target_ip = "172.16.67.144"
target_port = 80
source_port = 12345

# Create a TCP SYN packet (https://scapy.readthedocs.io/en/latest/)
syn_packet = IP(dst=target_ip) / TCP(sport=source_port, dport=target_port, flags="S")

# Send the SYN packets
for i in range(0, 50):
    send(syn_packet, verbose=True)
    time.sleep(0.1)
