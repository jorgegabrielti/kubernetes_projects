# Projeto 3: Secrets - Guardando Informações Sensíveis

## Objetivo: 
Criar e usar um Secret para armazenar credenciais de banco de dados.

Crie o arquivo **secrets.yaml**:

```yaml
---
apiVersion: v1
kind: Secret
metadata:
  name: meu-banco-dados-secrets
type: Opaque
stringData:
  usuario: admin
  senha: senha_super_secreta
Use code with caution.
Yaml
Implante o Secret:
kubectl apply -f secrets.yaml
Use code with caution.
Bash
Crie um Deployment que utilize o Secret:
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-com-secrets
spec:
  # ... (restante da configuração)
      containers:
      - name: meu-app
        image: sua-imagem-docker
        env:
        - name: DB_USUARIO
          valueFrom:
            secretKeyRef:
              name: meu-banco-dados-secrets
              key: usuario
        - name: DB_SENHA
          valueFrom:
            secretKeyRef:
              name: meu-banco-dados-secrets
              key: senha
...
```

**Documentação**:

- [Usando Secrets como Variáveis de Ambiente](https://kubernetes.io/docs/concepts/configuration/secret/)

- [Configure a Pod to Use a ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#use-environment-variables-to-consume-the-data-in-a-secret)

>[!IMPORTANT]
Utilize ferramentas como kubectl create secret generic para criar Secrets interativamente.
Explore outros tipos de Secrets, como docker-registry para armazenar credenciais de registro Docker.
Considere soluções de gerenciamento de Secrets mais robustas para cenários de produção.