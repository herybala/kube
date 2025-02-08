FROM python:3.10.12-slim

WORKDIR /api
COPY . /api
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

CMD ["uvicorn", "wsgi:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]