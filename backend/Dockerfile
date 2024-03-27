# Use Python base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY ./backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY ./backend .

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
