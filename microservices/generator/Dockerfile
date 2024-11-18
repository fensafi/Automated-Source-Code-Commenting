# comment-generation-microservice/Dockerfile

# Use a slim Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files to the container
COPY . .

# Expose ports for FastAPI and TCP communication
EXPOSE 8002     
EXPOSE 17001    

# Start FastAPI app on port 8002
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]
