# Base image
FROM python:3.11-slim

# ตั้ง working directory
WORKDIR /app

# ติดตั้ง unzip, curl สำหรับดาวน์โหลด SonarScanner
RUN apt-get update && apt-get install -y unzip curl && rm -rf /var/lib/apt/lists/*

# คัดลอก requirements และติดตั้ง Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ด FastAPI เข้า container
COPY . .

# ดาวน์โหลดและติดตั้ง SonarScanner CLI
RUN curl -sSLo sonar-scanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.9.3.74484-linux.zip \
    && unzip sonar-scanner.zip -d /opt \
    && rm sonar-scanner.zip

# เพิ่ม SonarScanner เข้า PATH
ENV PATH="/opt/sonar-scanner-4.9.3.74484-linux/bin:${PATH}"

# เปิด port สำหรับ FastAPI
EXPOSE 8000

# รัน FastAPI ด้วย uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
