# simple-flask-app-ubuntu

A simple Flask application built on Ubuntu, containerized with Docker, and managed with Git/GitHub as part of my cloud development learning path.

## Features

- Flask web app
- `/health` endpoint
- Dockerized for local testing
- Built and managed from Ubuntu terminal

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run --host=0.0.0.0 --port=5000
```

## Run with Docker

```bash
docker build -t simple-flask-app:v1 .
docker run --rm -p 5000:5000 simple-flask-app:v1
```

## Endpoints

- `/`
- `/health`
