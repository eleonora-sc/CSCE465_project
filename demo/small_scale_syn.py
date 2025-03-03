from scapy.all import IP, TCP, send
import time

# Target details
<<<<<<< HEAD:socket_library/small_scale_syn.py
target_ip = "127.0.0.1"
=======
target_ip = "172.16.98.225" 
>>>>>>> d02d2dbd574b0f62656a728af2765515cc070918:demo/small_scale_syn.py
target_port = 80

# Create a TCP SYN packet (https://scapy.readthedocs.io/en/latest/)
syn_packet = IP(dst=target_ip) / TCP(dport=target_port, flags="S")

<<<<<<< HEAD:socket_library/small_scale_syn.py
# Send the SYN packet
for i in range(0, 50):
    send(syn_packet, verbose=True)
    time.sleep(0.3)
=======
# Send the SYN packets
for i in range (0,30):
    send(syn_packet, verbose=True)
    time.sleep(0.33)
>>>>>>> d02d2dbd574b0f62656a728af2765515cc070918:demo/small_scale_syn.py
