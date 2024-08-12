# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies specified in requirements.txt
# (if you have one, otherwise skip this step)
# RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "coffe_machine.py"]
