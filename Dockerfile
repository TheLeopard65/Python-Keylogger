FROM python:3.10-slim
WORKDIR /app
COPY keylogger.py .
COPY .env .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "keylogger.py"]
