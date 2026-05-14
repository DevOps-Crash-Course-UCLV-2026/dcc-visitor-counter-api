FROM python:3.7-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install build deps (kept minimal) and requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

EXPOSE 5000

# Use gunicorn to run the Flask app defined in main.py
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
