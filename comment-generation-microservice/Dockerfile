# Use the official Python 3.8 slim image from Docker Hub as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file from the correct location
COPY ./comment-generation-microservice/requirements.txt /app/requirements.txt

# Install the dependencies listed in the requirements.txtfile
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy all other files after installing dependencies
COPY . .

# Run the FastAPI app using Uvicorn when the container starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]
