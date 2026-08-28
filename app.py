from flask import Flask, jsonify
import os
import platform
from datetime import datetime, timezone

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "message": "DevOps Python Practice API",
        "status": "running",
        "hostname": platform.node(),
        "environment": os.getenv("APP_ENV", "development")
    })

@app.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.get("/info")
def info():
    return jsonify({
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "hostname": platform.node()
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)

