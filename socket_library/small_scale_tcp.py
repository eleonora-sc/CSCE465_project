import time
import threading
import requests

def send_requests():
    url = "http://172.16.98.225"
    for i in range(0,10):
        time.sleep(0.2)
        try:
            response = requests.get(url)
            print(i)
        except Exception as e:
            print(f"Request failed: {e}")

if __name__ == '__main__':
    send_requests()
