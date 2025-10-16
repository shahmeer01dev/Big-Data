# Dockerfile

# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install the hdfs library
RUN pip install hdfs

# CMD ["python", "main.py"]  <-- Comment this line out