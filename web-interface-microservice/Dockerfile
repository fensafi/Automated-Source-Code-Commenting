# web-interface-microservice/Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8004 

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8004"]
