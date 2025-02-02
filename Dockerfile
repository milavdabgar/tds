FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY api/ api/
COPY vercel.json .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api.index:app", "--host", "0.0.0.0", "--port", "8000"]
