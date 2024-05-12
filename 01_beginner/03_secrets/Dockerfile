FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV MYSQL_HOST=mysql-service
ENV MYSQL_DATABASE=mydb

EXPOSE 5000

CMD ["python", "app.py"]