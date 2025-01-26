FROM python:3.11-slim

WORKDIR /app

COPY reqs.txt .
RUN pip install --no-cache-dir -r reqs.txt

COPY . .

EXPOSE 8008

CMD ["bash", "-c", "python -m scripts.download_models && python -m api.main"]
