# Pull base image for python
FROM python:3.8-slim 

# Set the workig directory in the image
WORKDIR /app

# Copy the current directory contents at /app in the image
COPY . /app

# Run the application
CMD ["python", "app.py"]