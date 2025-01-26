FROM python:3.11-slim

WORKDIR /app

COPY reqs.txt .
RUN pip install --no-cache-dir -r reqs.txt

COPY api/ ./api/
COPY scripts/ ./scripts/

RUN python3 scripts/download_models.py

EXPOSE 8008

WORKDIR /app/api

CMD ["python", "-m", "main"]
