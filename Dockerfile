# Use an official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy application files
COPY app.py .

# Install dependencies
RUN pip install flask prometheus_client

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
