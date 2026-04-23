from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello from your Dockerized Flask app on Ubuntu!"

@app.route("/health")
def health ():
	return{"status": "ok"}
