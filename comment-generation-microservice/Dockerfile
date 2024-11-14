# Use the official Python 3.8 slim image from Docker Hub as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements1.txt file from the correct location
COPY ./comment-generation-microservice/requirements1.txt /app/requirements1.txt

# Install the dependencies listed in the requirements.txt file
RUN pip install --no-cache-dir -r /app/requirements1.txt

# Copy all other files after installing dependencies
COPY . .

# Run the FastAPI app using Uvicorn when the container starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]
