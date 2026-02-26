# Pull the base image for python
FROM python:3.8-slim

# Set the working directory in the image
WORKDIR /app

# Copy the current directory contents at /app in the image
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the application will run on
EXPOSE 5000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]