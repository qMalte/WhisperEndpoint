FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY src/main.py .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]