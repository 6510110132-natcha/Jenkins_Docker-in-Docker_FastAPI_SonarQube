# Base image Python 3.11 slim
FROM python:3.11-slim

# ตั้ง working directory
WORKDIR /app

# ติดตั้ง unzip, curl (ใช้ดาวน์โหลด SonarScanner)
RUN apt-get update && apt-get install -y unzip curl && rm -rf /var/lib/apt/lists/*

# คัดลอก requirements.txt และติดตั้ง dependencies
COPY fastapi-app/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดทั้งหมดเข้า container
COPY fastapi-app/ ./fastapi-app

# ดาวน์โหลดและติดตั้ง SonarScanner
RUN curl -sSLo sonar-scanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.9.3.74484-linux.zip \
    && unzip sonar-scanner.zip -d /opt \
    && rm sonar-scanner.zip

ENV PATH="/opt/sonar-scanner-4.9.3.74484-linux/bin:${PATH}"

# เปิด port 8000
EXPOSE 8000

# รัน FastAPI ด้วย uvicorn
CMD ["uvicorn", "fastapi-app.main:app", "--host", "0.0.0.0", "--port", "8000"]
