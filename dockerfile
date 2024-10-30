FROM python:3.9-slim
LABEL maintainer="Varun Samaga"
LABEL roll="21BCS129"

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]

