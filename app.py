import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_MESSAGE = os.getenv("APP_MESSAGE", "Hello from Flask on Ubuntu + Docker!")

@app.route("/")
def home():
    return APP_MESSAGE

@app.route("/health")
def health():
    return jsonify(status="ok")
