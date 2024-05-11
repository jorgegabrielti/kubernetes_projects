# Projeto 1: "Olá, Kubernetes!" - Sua primeira aplicação web

## Objetivo:

Implantar um simples servidor web Nginx e expor publicamente via serviço NodePort.

Crie o arquivo **deployment.yaml**:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: meu-nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
```

Crie o arquivo **service.yaml**:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: meu-nginx-service
spec:
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: LoadBalancer
```

Implante no cluster:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

```bash
kubectl get service meu-nginx-service
```
### Anote o EXTERNAL-IP e acesse no navegador

**Documentação**:

- [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Tipos de Serviço](https://cloud.google.com/kubernetes-engine/docs/concepts/service?hl=pt-br) (Observe as diferenças entre LoadBalancer, NodePort e ClusterIP)

>[!IMPORTANT]
Experimente diferentes imagens Docker, como httpd para Apache.
Ajuste o número de réplicas no Deployment para observar o escalonamento automático.
Explore alternativas ao LoadBalancer, como por exemplo, NodePort, se não estiver em um ambiente de nuvem.