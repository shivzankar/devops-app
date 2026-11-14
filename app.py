from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from {os.getenv('APP_COLOR','v1')} | build {os.getenv('BUILD','dev')}\n"

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
