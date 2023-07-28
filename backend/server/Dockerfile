# syntax=docker/dockerfile:1
# Use an official Python runtime as a base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /server

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app's files into the container
COPY . .

# Expose the port your Flask app is running on (change 5000 to your app's port if needed)
EXPOSE 5000

# Define the command to run your Python application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]