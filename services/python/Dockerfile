FROM python:3.7.2-alpine

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
    apk update && \
    apk add --no-cache \
        gcc

ENV FLASK_APP app.py
ENV FLASK_DEBUG 1
ENV FLASK_RUN_HOST 0.0.0.0

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
