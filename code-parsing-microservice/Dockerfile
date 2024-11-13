# Use the official Python 3.8 slim image from Docker Hub as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory (where Dockerfile is located) into the container's /app directory
COPY . .

# Install the dependencies listed in the requirements.txt file
RUN pip install -r requirements.txt

# Run the FastAPI app using Uvicorn when the container starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
