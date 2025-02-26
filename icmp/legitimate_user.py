from scapy.all import IP, ICMP, send, sr1
import random


def send_icmp_request(target_ip, packet_size):
    packet = IP(dst=target_ip) / ICMP() / ("X" * packet_size) 
    print(f"Sent ICMP Request to {target_ip} with size {packet_size} bytes")

    response = sr1(packet, verbose=False) 
    
    if response:
        print(f"Received ICMP Reply from {response.src}: {response.summary()}")
    else:
        print(f"No response from {target_ip}")
        


if __name__ == "__main__":
    target_ip = "127.0.0.1" 
    packet_size = random.randint(1,65500)  

    send_icmp_request(target_ip, packet_size)