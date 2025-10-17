FROM python:3.10-slim

WORKDIR /app

# 운영 의존성만 설치
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 소스만 복사 (tests는 .dockerignore로 제외)
COPY app/. .

EXPOSE 5000
CMD ["python", "main.py"]

