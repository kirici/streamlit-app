FROM docker.io/library/python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY .streamlit/ .streamlit/

COPY main.py main.py

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
