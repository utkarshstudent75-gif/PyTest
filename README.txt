# Docker Practice Project

This is a small hands-on project you can use to practice common Docker commands.

## What is inside

- `app.py` - a tiny Python Flask app
- `requirements.txt` - Python dependencies
- `Dockerfile` - build a custom image
- `compose.yaml` - run the app with Docker Compose
- `.dockerignore` - reduce build context
- `PRACTICE.md` - command-by-command exercises

## Goal

Use this project to practice:

- building images
- listing images and containers
- running containers
- mapping ports
- naming containers
- viewing logs
- executing commands inside containers
- stopping and removing containers
- using environment variables
- using Docker Compose

## Quick start

### 1. Build the image

```bash
docker build -t docker-practice-app .
```

### 2. Run the container

```bash
docker run --name docker-lab -p 5000:5000 docker-practice-app
```

Open: http://localhost:5000

### 3. Stop it

```bash
docker stop docker-lab
```

## Practice flow

Open `PRACTICE.md` and work through the exercises in order.
