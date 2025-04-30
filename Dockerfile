FROM python:3.11-slim

RUN apt update && apt install -y ffmpeg curl && \
    pip install yt-dlp flask flask-cors && \
    mkdir /app

WORKDIR /app

COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]
