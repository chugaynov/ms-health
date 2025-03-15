# Docker

### 1. Создать билдер для buildx
docker buildx create --use

### 2. Собрать образ
docker buildx build --platform linux/amd64 -t {dockerhub-username}/ms-health:v1.0 .

### 3. Авторизоваться в Docker Hub
docker login

### 4. Отправить образ в Docker Hub
docker push {dockerhub-username}/ms-health:v1.0

### 5. Запустить контейнер
docker run -p 8080:8080 {dockerhub-username}/ms-health:v1.0
