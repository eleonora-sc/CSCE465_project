from flask import Flask, render_template_string
import time
import psutil
import os

app = Flask(__name__)

@app.route('/')
def home():
    start_time = time.time()  # Track request processing time

    time.sleep(2)

    # Get current process
    p = psutil.Process(os.getpid())

    ## Reduce server resources so it becomes overloaded quicker
    try:
        # Restrict  server to only 1 CPU core
        p.cpu_affinity([0])  
    except AttributeError:
        pass  # CPU affinity isn't available on all Windows versions

    # Reduce priority (makes Flask use fewer CPU resources)
    p.nice(psutil.IDLE_PRIORITY_CLASS)  

    #  Server resource data
    cpu_usage = psutil.cpu_percent(interval=0.1)  
    memory = psutil.virtual_memory()  
    load_avg = psutil.getloadavg()[0]  

    # Track processing delay
    processing_time = time.time() - start_time  

    # HTML template
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Server Status</title>
        <meta http-equiv="refresh" content="2">  <!-- Refreshes page every 2 seconds -->
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f4; text-align: center; }
            h1 { color: #333; }
            .status-box { background: white; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); display: inline-block; }
        </style>
    </head>
    <body>
        <h1>Server Status</h1>
        <div class="status-box">
            <p><strong>Status:</strong> Server is running!</p>
            <p><strong>CPU Usage:</strong> {{ cpu_usage }}%</p>
            <p><strong>Memory Usage:</strong> {{ memory_usage }}%</p>
            <p><strong>Load Average:</strong> {{ load_avg }}</p>
            <p><strong>Processing Time:</strong> {{ processing_time }} sec</p>
        </div>
    </body>
    </html>
    """

    return render_template_string(html_template, 
                                  cpu_usage=cpu_usage, 
                                  memory_usage=memory.percent, 
                                  load_avg=load_avg, 
                                  processing_time=f"{processing_time:.3f}")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
