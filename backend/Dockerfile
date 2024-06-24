FROM python:3.12-slim

WORKDIR /backend

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080

COPY . .

ENV SQLALCHEMY_DATABASE_URI=sqlite:////app/data/whichllm.db

VOLUME /backend/data

CMD ["python", "app.py"]