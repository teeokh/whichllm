FROM python:3.12-slim

WORKDIR /backend

COPY backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

VOLUME /backend/data

CMD ["python", "app.py"]