from scapy.all import IP, ICMP, send, sr1
from multiprocessing import Process


def send_icmp_requests(target_ip, packet_size):
    for i in range(0,10):
        packet = IP(dst=target_ip) / ICMP() / ("X" * packet_size)  # Custom payload
        print(f"Sent ICMP Request to {target_ip} with size {packet_size} bytes")

        response = send(packet, verbose=False)  # Wait for a reply
        
        if response:
            print(f"Received ICMP Reply from {response.src}: {response.summary()}")
        else:
            print(f"No response from {target_ip}")
        


if __name__ == "__main__":
    target_ip = "172.16.98.225"
    packet_size = 1024  # Size in bytes

    send_icmp_requests(target_ip, packet_size)
