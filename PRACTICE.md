# Docker Practice Exercises

Use these commands one by one and observe what changes.

## 1. Build an image

```bash
docker build -t docker-practice-app .
```

## 2. List images

```bash
docker images
```

## 3. Run a container in the foreground

```bash
docker run --name docker-lab -p 5000:5000 docker-practice-app
```

## 4. Run a container in detached mode

```bash
docker run -d --name docker-lab -p 5000:5000 docker-practice-app
```

## 5. List running containers

```bash
docker ps
```

## 6. List all containers

```bash
docker ps -a
```

## 7. View logs

```bash
docker logs docker-lab
```

Follow logs live:

```bash
docker logs -f docker-lab
```

## 8. Execute a command inside the container

```bash
docker exec -it docker-lab sh
```

Inside the container, try:

```bash
ls
printenv
cat /etc/hostname
```

## 9. Inspect container details

```bash
docker inspect docker-lab
```

## 10. Stop the container

```bash
docker stop docker-lab
```

## 11. Start it again

```bash
docker start docker-lab
```

## 12. Remove the container

```bash
docker rm -f docker-lab
```

## 13. Run with a custom environment variable

```bash
docker run -d --name docker-lab -p 5000:5000 -e APP_ENV=testing docker-practice-app
```

Then open `http://localhost:5000` and check the `environment` value.

## 14. Use Docker Compose

Start:

```bash
docker compose up --build
```

Detached:

```bash
docker compose up -d --build
```

List:

```bash
docker compose ps
```

Logs:

```bash
docker compose logs -f
```

Stop and remove:

```bash
docker compose down
```

## 15. Cleanup images

```bash
docker rmi docker-practice-app
```

## Extra challenges

- Change the message in `app.py` and rebuild the image.
- Change the app port from 5000 to 8000.
- Add another route like `/about`.
- Try `docker rename docker-lab my-container`.
- Try `docker stats` while the container is running.
- Try `docker top docker-lab`.
- Try mounting the current folder with `-v $(pwd):/app`.
