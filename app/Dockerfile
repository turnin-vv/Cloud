FROM python:3.9-alpine3.17

RUN apk update && \
    apk upgrade && \
    apk add --no-cache build-base

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]