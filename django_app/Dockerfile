FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Environment variables (best practice)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run migrations (IMPORTANT for Render)
# collectstatic for static files
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput

# Expose port (optional but good practice)
EXPOSE 8000

# Start server using Render PORT
CMD ["sh", "-c", "gunicorn super_todo.wsgi:application --bind 0.0.0.0:$PORT"]
