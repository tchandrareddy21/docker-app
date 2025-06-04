# 🚀 Dockerized FastAPI App
- This is a lightweight, containerized web application built with FastAPI, using Redis as a backend service. The app runs on a Uvicorn server and is fully managed using Docker and Docker Compose.

## Docker Archtecture
![Docker Architecture](./docker%20architecture.svg)

## 📦 Stack
- FastAPI – Modern, fast (high-performance) web framework for building APIs
- Redis – In-memory key-value data store
- Uvicorn – ASGI web server for FastAPI
- Docker – For containerization
- Docker Compose – To orchestrate multi-container applications

## 🚀 Getting Started

### 📥 1. Clone or Download docker-compose.yml
If you're only using the Docker image (and don't have the app source), just download the docker-compose.yml:

```bash
curl -O https://raw.githubusercontent.com/tchandrareddy21/docker-app/refs/heads/main/docker-compose.yaml
```
Or clone the repo:

```bash
git clone https://github.com/tchandrareddy21/docker-app.git
cd docker-app
```
### ▶️ 2. Run the App

```bash
docker compose up -d
```
- This will:
    - Pull the FastAPI app image from Docker Hub
    - Pull the official Redis image
    - Start both services
    - Expose the app on http://localhost:8000

### 🔍 3. Test the API
Open your browser or a tool like Postman, and visit:

- Docs UI: http://localhost:8000/docs
- Root endpoint: http://localhost:8000
- Hit count endpoint: http://localhost:8000/hit_count

## 🧹 Cleanup
To stop and remove all containers:

```bash
docker compose down
```
