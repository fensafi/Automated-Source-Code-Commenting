# Use the official Python 3.8 slim image from Docker Hub as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first to leverage Docker's cache mechanism
COPY ${REQUIREMENTS_FILE} /app/requirements.txt

# Install the dependencies listed in the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy all other files after installing dependencies
COPY . .

# Run the FastAPI app using Uvicorn when the container starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
