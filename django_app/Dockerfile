FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

# HAPUS EXPOSE 8000 (Render akan mendeteksi port otomatis)
# Ubah CMD agar menggunakan port variabel $PORT yang disediakan Render
CMD ["sh", "-c", "gunicorn super_todo.wsgi:application --bind 0.0.0.0:$PORT"]
