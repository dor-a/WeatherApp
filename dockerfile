# Use Python 3.9 Alpine base image
FROM python:3.9-alpine


RUN apk update && apk add --no-cache \
    && rm -rf /var/cache/apk/*

WORKDIR /app


COPY requirements.txt main.py .env /app/

RUN pip install --no-cache-dir -r requirements.txt


ENTRYPOINT ["python", "main.py"]
