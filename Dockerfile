# Pull base image
FROM python:3.11-alpine

# Set working directory
WORKDIR /

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt /
RUN pip install -r requirements.txt && pip cache purge

# Copy source code
COPY . /

# Run the application
CMD ["python3", "bot.py"]