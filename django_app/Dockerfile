FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN migrations + collectstatic saat build (opsional)
# Bisa juga jalankan di CMD agar migrate selalu jalan saat start
# RUN python manage.py migrate --noinput
# RUN python manage.py collectstatic --noinput

EXPOSE 8000

# CMD versi stabil untuk Render free plan + SQLite
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn super_todo.wsgi:application --bind 0.0.0.0:$PORT"]
