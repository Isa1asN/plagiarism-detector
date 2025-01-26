FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    && apt-add-repository contrib \
    && apt-get update \
    && apt-get install -y unrar \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY reqs.txt .
RUN pip install --no-cache-dir -r reqs.txt

COPY api/ ./api/
COPY scripts/ ./scripts/

RUN python3 scripts/download_models.py

COPY models/ ./models/

EXPOSE 8008

WORKDIR /app/api

CMD ["python", "-m", "main"]
