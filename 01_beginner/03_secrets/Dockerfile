FROM python:3.9-slim-buster

WORKDIR /app

RUN apt update -y && \
    apt install -y pkg-config python3-dev default-libmysqlclient-dev build-essential && \

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV MYSQL_HOST=mysql-service
ENV MYSQL_DATABASE=mydb

EXPOSE 5000

CMD ["python", "app.py"]