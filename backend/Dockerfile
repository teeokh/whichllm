FROM python:3.12-slim

WORKDIR /backend

COPY backend/requirements.txt .
COPY backend/app.py .

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
COPY backend/ .

VOLUME /backend/data

CMD ["python", "./backend/app.py"]