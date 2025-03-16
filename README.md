# Docker

## Сборка для размещения в DockerHub под AMD64 (Инструкция)
### 1. Создать билдер для buildx
```shell
docker buildx create --use
```

### 2. Собрать образ
```shell
docker buildx build --platform linux/amd64 -t {dockerhub-username}/ms-health:v1.0 .
```

### 3. Авторизоваться в Docker Hub
```shell
docker login
```

### 4. Отправить образ в Docker Hub
```shell
docker push {dockerhub-username}/ms-health:v1.0
```

### 5. Запустить контейнер
```shell
docker run -p 8080:8080 {dockerhub-username}/ms-health:v1.0
```


## Готовые примеры
### DockerHub сборка под AMD64
```shell
docker buildx create --use
docker buildx build --platform linux/amd64 -t achugaynov/ms-health:v1.0 .
docker login
docker push achugaynov/ms-health:v1.0
docker run -p 8080:8080 achugaynov/ms-health:v1.0
```

### Локальная сборка под ARM64
```shell
docker buildx build --platform linux/arm64 -t achugaynov/ms-health:v1.0 --load .
docker run -p 8080:8080 achugaynov/ms-health:v1.0
```
