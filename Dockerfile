# Dockerfile
FROM python:alpine3.17

WORKDIR /app

COPY requirements.txt .env ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./chat.py" ]
