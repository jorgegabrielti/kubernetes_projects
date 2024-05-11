# Projeto 2: Escalando Aplicações - Ajuste Dinâmico para Demanda

## Objetivo: Criar um Deployment com escalonamento automático baseado em uso de CPU.

Crie o arquivo **deployment.yaml** (similar ao anterior, mas com um Pod que gera carga):

```yaml
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: stress-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: stress
  template:
    metadata:
      labels:
        app: stress
    spec:
      containers:
      - name: stress
        image: polinux/stress
        resources:
          requests:
            cpu: 100m
        command: ["stress", "--cpu", "1"]
...
```

Crie o arquivo **hpa.yaml** para o **HorizontalPodAutoscaler**:

```yaml
---
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: stress-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: stress-app
  minReplicas: 1
  maxReplicas: 5
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
...
```

Implante:
```bash
kubectl apply -f deployment.yaml
kubectl apply -f hpa.yaml
```

Monitore:
```bash
kubectl get hpa stress-app-hpa
kubectl top pods
```

**Documentação**:
- [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
- [Especificando Recursos de CPU](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-cpu)

>[!IMPORTANT]
Ajuste os valores de **averageUtilization** e limites de réplicas no HPA.
Utilize outras métricas de escalonamento além da CPU, como memória ou requests personalizadas.