from flask import Flask
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return {
        "message": "Hello from your Docker practice app!",
        "container_hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "not set"),
        "time": datetime.utcnow().isoformat() + "Z"
    }

@app.route('/health')
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
