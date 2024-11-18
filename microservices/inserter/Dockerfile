# comment-insertion-microservice/Dockerfile

# Use a slim Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files to the container
COPY . .

# Expose the port for FastAPI
EXPOSE 8003      

# Start FastAPI app on port 8003
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8003"]
