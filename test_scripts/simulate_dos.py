from flask import Flask
import time
import threading
import requests

app = Flask(__name__)

@app.route('/')
def home():
    time.sleep(0.1)  # Simulate processing delay
    return "Server is running!"

def send_requests():
    url = "http://127.0.0.1:5000/"
    while True:
        try:
            response = requests.get(url)
            print(response.text)
        except Exception as e:
            print(f"Request failed: {e}")

if __name__ == '__main__':
    threading.Thread(target=send_requests, daemon=True).start()
    app.run(host='127.0.0.1', port=5000, threaded=True)  # Enable threading to handle multiple requests
