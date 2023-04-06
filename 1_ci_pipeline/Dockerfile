# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the file to the container
COPY requirements.txt .
COPY users.json .

# Install the app's dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files to the container
COPY app app

# Set the FLASK_APP environment variable
ENV FLASK_APP=app/main.py

# Expose the port on which the app will run
EXPOSE 5000

# Start the app
CMD ["flask", "run", "--host=0.0.0.0"]