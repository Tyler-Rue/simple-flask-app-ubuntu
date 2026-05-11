# simple-flask-app-ubuntu

A simple Flask application built on Ubuntu, containerized with Docker, and managed with Git/GitHub as part of my cloud development learning path.

## Features

- Flask web app
- `/health` endpoint
- Dockerized for local testing
- Built and managed from Ubuntu terminal
- Prepared GitHub Actions workflow for Azure Container Apps deployment

## GitHub Actions Deployment Workflow

This repo includes a manual GitHub Actions workflow for deploying the Flask container image to Azure Container Apps.

The workflow is designed to:

1. Authenticate to Azure using OIDC
2. Build the Docker image
3. Push the image to Azure Container Registry
4. Update the Azure Container App image

The workflow is currently manual (`workflow_dispatch`) so deployments only occur intentionally.

Required Azure resources before running the workflow:

- Azure Container Registry
- Azure Container App
- Container Apps Environment
- Resource group configured in repository variables

## Deployment Notes

The Azure deployment workflow is prepared for future use after the required Azure resources are recreated. This keeps the repo ready for CI/CD deployment while avoiding unnecessary cloud resource costs when the app is not actively being tested.

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
