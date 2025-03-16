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


# Kubernetes
### Kubectl reference
https://kubernetes.io/docs/reference/kubectl/generated/

### Применить настройки деплоймента и сервиса
```shell
kubectl delete deployment ms-health-deployment
kubectl delete service ms-health-service
kubectl delete ingress ms-health-ingress

kubectl describe pod nginx-ingress-nginx-controller-s8cdr -n nginx
```

```shell
kubectl create namespace dev
kubectl apply -f k8s/.
```

# Nginx Ingress из helm
```shell
kubectl create namespace nginx && \
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx/ && \
helm repo update && \
helm install nginx ingress-nginx/ingress-nginx --namespace nginx -f k8s/nginx-ingress.yaml
```

# Kubernetes на CLO RU
https://clo.ru/help/containerization/installation
