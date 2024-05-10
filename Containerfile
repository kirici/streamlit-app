FROM docker.io/library/python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY .streamlit/ .streamlit/

COPY main.py main.py

CMD ["streamlit", "run", "main.py"]
