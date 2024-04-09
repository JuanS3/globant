FROM python:3.11-slim

ENV DATABASE_USER=globanTest
ENV DATABASE_PASS=mypassword
ENV DATABASE_NAME=employees_jobs
ENV DATABASE_TYPE=postgresql
ENV DATABASE_HOST=localhost
ENV DATABASE_PORT=5432

WORKDIR /app

COPY app/ .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
