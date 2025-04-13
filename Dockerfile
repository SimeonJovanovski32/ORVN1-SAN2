# Use a Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from your repository to the /app directory inside the container
COPY . .

# Install any Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for Python
ENV PYTHONUNBUFFERED=1

# Run the application or provide a command when the container starts
CMD ["python", "naloga1.py"]
