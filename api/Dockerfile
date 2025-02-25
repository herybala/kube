FROM python:3.10.12-slim

WORKDIR /api
COPY requirements.txt /api
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["uvicorn", "wsgi:app", "--reload", "--workers", "3", "--host", "0.0.0.0", "--port", "5000"]